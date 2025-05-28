# Common Python Input Strategies for Advent of Code

Advent of Code (AoC) problems often come with various input formats. Efficiently parsing these inputs is crucial for solving problems quickly and accurately. Below are common strategies and code snippets for handling typical AoC input formats in Python.

---

## 1. Reading the Entire File as Lines

```python
with open('input.txt') as f:
    lines = f.read().splitlines()
```
- **Use when:** Each line is a separate value or record.
- **Example:**
  ```
  123
  456
  789
  ```

---

## 2. Splitting Input into Sections (by Blank Line)

```python
with open('input.txt') as f:
    sections = f.read().strip().split('\n\n')
```
- **Use when:** The input has multiple blocks separated by blank lines.
- **Example:**
  ```
  1\n2\n3\n\n4\n5\n6
  ```
  - `sections[0]` is '1\n2\n3'
  - `sections[1]` is '4\n5\n6'

---

## 3. Parsing Numbers from Input

**Single line of numbers:**
```python
numbers = list(map(int, lines[0].split(',')))
```
**Multiple lines of numbers:**
```python
numbers = [int(line) for line in lines]
```
**2D grid of numbers:**
```python
grid = [list(map(int, line)) for line in lines]
```

---

## 4. Parsing Rules or Key-Value Pairs

**Example line:** `A -> B`
```python
rules = {}
for line in lines:
    key, value = line.split(' -> ')
    rules[key] = value
```
**Example line:** `12|34`
```python
rules = {}
for line in lines:
    left, right = line.split('|')
    rules[int(left)] = int(right)
```

---

## 5. Advanced: Grouping and Custom Parsing

When input blocks have headers or mixed formats, use manual parsing:
```python
with open('input.txt') as f:
    lines = f.read().splitlines()

blocks = []
block = []
for line in lines:
    if line.strip() == '':
        if block:
            blocks.append(block)
            block = []
    else:
        block.append(line)
if block:
    blocks.append(block)
```
- Now, `blocks` is a list of lists, each representing a section.

---

## 6. Reading Input as a Single String

```python
with open('input.txt') as f:
    content = f.read()
```
- **Use when:** The input is a single string or needs regex parsing.

---

## Tips
- Always inspect your input and adapt your parsing logic.
- Print intermediate results to debug parsing.
- Use `strip()` to remove unwanted whitespace.

---

## References
- [Official AoC Python Tips](https://github.com/wimglenn/advent-of-code-wim/blob/main/README.md#python-tips)
- [Python Input Cookbook](https://realpython.com/read-write-files-python/)

---

Happy coding and good luck with Advent of Code!
