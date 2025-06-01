# Coding Best Practices & Debugging Guide

## 1. Problem Understanding & Planning

Before writing any code:
- Read the problem 2-3 times carefully
- Identify edge cases upfront (empty inputs, boundary values, impossible cases)
- Trace through examples manually on paper
- Write pseudocode or outline your approach first

## 2. Systematic Debugging Process

### Test with Provided Examples
```python
if __name__ == "__main__":
    sol = Solution()
    # Test all provided examples
    print(sol.canMeasureWater(3, 5, 4))  # Expected: True
    print(sol.canMeasureWater(2, 6, 5))  # Expected: False
```

### Use Print Statements Liberally
```python
def dfs(curX, curY):
    print(f"Visiting state: ({curX}, {curY})")
    if curX + curY == target:
        print(f"Found target!")
        return True
```

## 3. Code Structure Best Practices

### Handle Edge Cases First
```python
def canMeasureWater(self, x, y, target):
    # Edge cases at the top, always!
    if target > x + y:
        return False
    if target == 0:
        return True
    # ... rest of logic
```

### Use Early Returns
```python
# Instead of computing all cases
if case1:
    return True
if case2:
    return True
# ...
```

## 4. Common Bug Categories

### Syntax Bugs
- Always use an IDE/editor with syntax highlighting
- Run code frequently - don't write 50 lines then test
- Common mistakes: missing parentheses, = vs ==, wrong operators

### Logic Bugs
- Off-by-one errors: Check boundary conditions
- Wrong initial states: Always verify starting conditions
- Incorrect loop/recursion termination: Add base cases first

### Algorithmic Bugs
- Missing visited sets in DFS/BFS (infinite loops)
- Wrong conditions for state transitions
- Not handling all possible operations

## 5. Development Workflow

### Incremental Development
1. Write basic structure with edge cases
2. Test edge cases
3. Add one operation at a time
4. Test after each addition
5. Refactor when working

### Example Progression
```python
# Step 1: Just structure and edge cases
def canMeasureWater(self, x, y, target):
    if target > x + y: return False
    if target == 0: return True
    return False  # Placeholder

# Step 2: Add basic DFS structure
def dfs(curX, curY):
    if curX + curY == target: return True
    return False
```

## 6. Specific Techniques

### Type Hints & Documentation
```python
def canMeasureWater(self, x: int, y: int, target: int) -> bool:
    """
    Returns whether we can measure exactly 'target' liters.
    Start with both jugs empty.
    """
```

### Assertion Checking
```python
def pour_x_to_y(cur_x: int, cur_y: int, max_y: int) -> tuple[int, int]:
    assert cur_x >= 0 and cur_y >= 0
    assert cur_y <= max_y
    pour_amount = min(cur_x, max_y - cur_y)
    return (cur_x - pour_amount, cur_y + pour_amount)
```

### Unit Test Mindset
```python
def test_pour_operations():
    # Test pouring logic separately
    assert pour_x_to_y(3, 2, 5) == (0, 5)  # Pour all of X
    assert pour_x_to_y(4, 3, 5) == (2, 5)  # Fill Y completely
```

## 7. Tools & Environment

- Use Python with good IDE: VS Code, PyCharm
- Enable linting: Catches syntax errors before running
- Use debugger: Step through code line by line
- LeetCode playground: Test immediately

## 8. Mental Checklist Before Submitting

- [ ] Did I handle all edge cases?
- [ ] Did I test with provided examples?
- [ ] Does my solution handle the boundary conditions?
- [ ] Am I starting from the correct initial state?
- [ ] Do I have proper cycle detection (for graph problems)?
- [ ] Are my variable names clear and consistent?

## 9. Learn from Each Bug

Keep a bug journal:
- "Forgot closing parenthesis - need to run code more frequently"
- "Started with wrong initial state - always verify problem constraints"
- "Overcomplicated conditions - simplify logic step by step"

The key is to slow down and be systematic. Most bugs come from rushing through the implementation without fully understanding the problem or testing incrementally.
