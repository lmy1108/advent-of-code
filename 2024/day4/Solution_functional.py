"""
Day 4: Ceres Search (Functional Programming Version)

This solution demonstrates how to approach the word search problem using functional programming concepts in Python.

Key Concepts Used:
- Pure functions: All helper functions are stateless and deterministic.
- Immutability: No mutation of input data.
- Higher-order functions: Functions are passed as arguments and used in comprehensions.
- List/generator comprehensions: Used instead of explicit loops and accumulators.
- No side effects: All computation is done via return values.

Compare this with the imperative version for clarity and maintainability!
"""
from typing import List

def read_grid(filename: str) -> List[List[str]]:
    with open(filename, encoding='utf-8') as f:
        return [list(line.strip()) for line in f if line.strip()]

def match(grid: List[List[str]], word: str, x: int, y: int, dx: int, dy: int) -> bool:
    """
    Checks if 'word' appears in grid starting at (x, y) in direction (dx, dy).
    Pure function: no state is modified.
    """
    rows, cols = len(grid), len(grid[0])
    return all(
        0 <= x + dx*i < rows and 0 <= y + dy*i < cols and grid[x + dx*i][y + dy*i] == word[i]
        for i in range(len(word))
    )

def count_word_occurrences(grid: List[List[str]], word: str) -> int:
    """
    Counts all occurrences of 'word' in any direction in the grid.
    Uses generator comprehensions for a functional approach.
    """
    steps = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    rows, cols = len(grid), len(grid[0])
    return sum(
        1
        for x in range(rows)
        for y in range(cols)
        for dx, dy in steps
        if match(grid, word, x, y, dx, dy)
    )

if __name__ == '__main__':
    grid = read_grid('input.txt')
    print(count_word_occurrences(grid, 'XMAS'))

"""
Explanation of Functional Concepts:

- Pure Functions: Each function's output depends only on its input. For example, 'match' and 'count_word_occurrences' do not modify any external state.
- Immutability: We do not change the grid or any input; we only compute and return values.
- Comprehensions: Instead of nested for-loops with mutation, we use generator comprehensions to express the search declaratively.
- No Side Effects: All functions return results; nothing is printed or mutated except in the __main__ guard.

Advantages:
- Easier to test and reason about.
- Fewer bugs from accidental mutation or state changes.
- More concise and expressive code.
"""
