# Python Sorting Guide

This guide covers the basics and intermediate usage of sorting in Python, including built-in functions and custom sorting techniques.

## Table of Contents
- [Basic Sorting](#basic-sorting)
- [Sorting with Custom Keys](#sorting-with-custom-keys)
- [Sorting with Multiple Criteria](#sorting-with-multiple-criteria)
- [Stability and Complex Sorts](#stability-and-complex-sorts)
- [Performance Considerations](#performance-considerations)
- [Common Patterns](#common-patterns)

## Basic Sorting

### Sorting Lists In-Place
```python
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sorts the list in-place
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]
```

### Creating a New Sorted List
```python
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # Returns a new sorted list
print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]
print(numbers)  # Original list remains unchanged
```

### Reverse Order
```python
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)  # Sorts in descending order
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]
```

## Sorting with Custom Keys

### Using `key` Function
```python
# Sort strings by length
fruits = ['apple', 'banana', 'cherry', 'date']
fruits.sort(key=len)
print(fruits)  # Output: ['date', 'apple', 'banana', 'cherry']

# Sort case-insensitive
names = ['Alice', 'bob', 'Charlie', 'dave']
names.sort(key=str.lower)
print(names)  # Output: ['Alice', 'bob', 'Charlie', 'dave']
```

### Using Lambda Functions
```python
# Sort list of tuples by second element
students = [('Alice', 90), ('Bob', 85), ('Charlie', 92)]
students.sort(key=lambda x: x[1])
print(students)  # Output: [('Bob', 85), ('Alice', 90), ('Charlie', 92)]
```

## Sorting with Multiple Criteria

### Using Tuples for Multiple Keys
```python
# Sort by name (ascending) then by score (descending)
students = [
    ('Alice', 90, 'A'),
    ('Bob', 85, 'B'),
    ('Charlie', 92, 'A'),
    ('Alice', 88, 'B')
]

# Sort by name (ascending), then by score (descending)
students.sort(key=lambda x: (x[0], -x[1]))
print(students)
# Output: [('Alice', 90, 'A'), ('Alice', 88, 'B'), ('Bob', 85, 'B'), ('Charlie', 92, 'A')]
```

### Using `operator.itemgetter`
```python
from operator import itemgetter

# Sort by index 1 (score) then by index 0 (name)
students.sort(key=itemgetter(1, 0))
```

## Stability and Complex Sorts

### Stable Sort Property
Python's sort is stable, meaning that items with equal keys maintain their relative order:

```python
# Sort by first letter, then by original position
items = ['banana', 'apple', 'cherry', 'date', 'apricot']
items.sort(key=lambda x: x[0])  # Sort by first character only
print(items)  # Output: ['apple', 'apricot', 'banana', 'cherry', 'date']
```

### Complex Custom Sorting
For more complex sorting, you can define a custom comparison function:

```python
from functools import cmp_to_key

def compare(a, b):
    # Custom comparison logic
    if a[1] != b[1]:  # First sort by second element
        return a[1] - b[1]
    else:  # If second elements are equal, sort by first element in reverse
        return b[0] - a[0]

data = [(1, 5), (3, 2), (2, 2), (4, 1)]
data.sort(key=cmp_to_key(compare))
print(data)  # Output: [(4, 1), (3, 2), (2, 2), (1, 5)]
```

## Performance Considerations

- `sorted()` creates a new list, while `list.sort()` sorts in-place
- Both functions have a time complexity of O(n log n)
- The `key` function is called exactly once for each input record
- For large datasets, consider using `operator` module functions instead of lambdas for better performance

## Common Patterns

### Sorting Dictionaries
```python
# Sort dictionary by value
scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(sorted_scores)  # Output: {'Charlie': 92, 'Alice': 90, 'Bob': 85}
```

### Sorting Objects
```python
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    
    def __repr__(self):
        return f"{self.name}: {self.grade}, {self.age}"

students = [
    Student('Alice', 'A', 20),
    Student('Bob', 'B', 19),
    Student('Charlie', 'A', 21)
]

# Sort by grade (ascending) then by age (descending)
students.sort(key=lambda s: (s.grade, -s.age))
print(students)
# Output: [Charlie: A, 21, Alice: A, 20, Bob: B, 19]
```

### Natural Sort for Strings with Numbers
```python
import re

def natural_sort_key(s):
    """
    Key function for natural sorting of strings containing numbers.
    Example: 'file2.txt' comes before 'file10.txt'
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

files = ['file1.txt', 'file10.txt', 'file2.txt', 'file20.txt']
files.sort(key=natural_sort_key)
print(files)  # Output: ['file1.txt', 'file2.txt', 'file10.txt', 'file20.txt']
```

This guide covers the most common sorting patterns in Python. The examples demonstrate how to handle various sorting scenarios, from basic to more complex cases.
