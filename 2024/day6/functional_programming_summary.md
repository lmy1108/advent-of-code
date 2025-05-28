# Functional Programming in Python: Grid Simulation Case Study

## Problem Overview

We tackled a grid simulation problem where a guard moves through a grid following specific rules:
- The guard can face in four directions (up, right, down, left)
- If the next cell is empty (`.` or `X`), the guard moves forward
- If the next cell is blocked (`#`), the guard turns right
- The simulation continues until the guard can't move

## Approaches and Challenges

### Initial Recursive Approach (Solution.py)

```python
def walk(grid: list[list[str]]) -> list[list[str]]:
    new_grid = [row.copy() for row in grid]
    # ... logic to move the guard ...
    return walk(new_grid)  # Recursive call
```

**Challenges:**
- **Recursion Depth**: Python has a limited recursion depth (~1000)
- **Memory Usage**: Creating a new grid copy for each step is expensive
- **Mutability Issues**: Confusion between `list[str]` and `list[list[str]]`

### Functional Approach with Immutable Data (solution_2.py)

```python
def walk(grid: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    def update_grid(grid, x, y, value):
        new_row = grid[x][:y] + (value,) + grid[x][y+1:]
        return grid[:x] + (new_row,) + grid[x+1:]
    # ... logic to move the guard ...
    return walk(new_grid)  # Recursive call
```

**Improvements:**
- **Immutability**: Using tuples instead of lists ensures data isn't accidentally modified
- **Pure Functions**: Each function returns a new state without side effects
- **Explicit State Transitions**: All changes are visible as new objects

### Iterative Solution (solution_2.py)

```python
def walk_iterative(grid: tuple[tuple[str, ...], ...], max_steps=10000):
    steps = 0
    while steps < max_steps:
        # Find guard position
        # Process based on direction
        # Create new grid with updates
        steps += 1
    return grid
```

**Benefits:**
- **No Recursion Limit**: Avoids Python's recursion depth limitation
- **Controlled Execution**: Can set a maximum step count to prevent infinite loops
- **Maintains Immutability**: Still uses immutable data structures

## Functional Programming Concepts

### 1. Immutable Data Structures

- **Tuples vs Lists**: Tuples are immutable, lists are mutable
- **Creating vs Modifying**: Always create new data rather than modifying existing data
- **Implementation**: `new_grid = update_grid(grid, x, y, 'X')`

### 2. Pure Functions

- **No Side Effects**: Functions don't modify external state
- **Deterministic**: Same inputs always produce same outputs
- **Composable**: Functions can be easily combined

### 3. Recursion vs Iteration

- **Tail Call Optimization**: Not available in Python (unlike Haskell)
- **Trampoline Pattern**: A way to simulate tail call optimization
- **Iterative Alternative**: Often more practical in Python

### 4. State Management

- **Explicit State Passing**: All state is passed as parameters
- **No Global Variables**: State is contained within function parameters
- **Immutable Updates**: Create new state objects rather than modifying existing ones

## Comparison with Haskell

The Haskell solution demonstrates several functional programming advantages:

```haskell
getPoints :: [String] -> Int -> Int -> (Int, Int) -> Int -> Set.Set (Int, Int) -> [(Int, Int)]
getPoints rows maxX maxY point dir visited 
    | x < 0 || x > maxX || y < 0 || y > maxY = Set.toList visited
    | rows !! y !! x == '#' = getPoints rows maxX maxY (getNextPoint point $ getOppositeDirection dir) (getTurnDirection dir) visited
    | otherwise = getPoints rows maxX maxY (getNextPoint point dir) dir (Set.insert point visited)
    where (x, y) = point
```

**Haskell Advantages:**
- **Tail Call Optimization**: Automatically converts tail-recursive calls to loops
- **Pattern Matching**: Elegant syntax for handling different cases
- **Efficient Immutable Data Structures**: Optimized for functional programming
- **Lazy Evaluation**: Only computes values when needed

## Practical Takeaways

1. **Choose the Right Tool**: Iterative approaches often work better in Python for complex recursion
2. **Be Explicit About Mutability**: Use type hints and appropriate data structures
3. **Consider Performance**: Immutable operations can be expensive for large data structures
4. **Hybrid Approaches**: Combine functional concepts with Python's strengths

## Resources for Further Learning

- [Real Python: Functional Programming in Python](https://realpython.com/python-functional-programming/)
- [Python's `functools` module](https://docs.python.org/3/library/functools.html)
- [Immutable data structures with `pyrsistent`](https://pyrsistent.readthedocs.io/)
- [Learn You a Haskell for Great Good](http://learnyouahaskell.com/) (for comparison with a purely functional language)
