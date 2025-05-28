# Functional Concepts in Scala Solution2.scala (Day 1, Part 2)

This document explains the key functional programming concepts demonstrated in `Solution2.scala` for Advent of Code Day 1, Part 2.

---

## Key Functional Concepts Used

### 1. **Immutability**
- All variables (such as `stringDigitReprs`, `digitReprs`, and `digitReprRegex`) are immutable (`val`), ensuring no accidental mutation.

### 2. **Pure Functions**
- The function `lineToCoordinates` is pure: its output depends only on its input, with no side effects or external state.
- The main computation in `part2` is also pure and stateless.

### 3. **Higher-Order Functions**
- `.map(lineToCoordinates(_))` applies the coordinate extraction function to each line, demonstrating the use of functions as first-class citizens.

### 4. **Declarative Collection Processing**
- Rather than using explicit loops and mutable accumulators, the solution uses Scala's collection methods (`linesIterator`, `map`, `sum`) to express the transformation and aggregation declaratively.

### 5. **Comprehensions**
- The `for`-comprehension over `line.tails` and `digitReprRegex.findPrefixOf(lineTail)` is a powerful and concise way to express nested iteration and filtering in a single, readable construct.
- This is analogous to Python's generator comprehensions, but more general.

### 6. **Pattern Matching via Regex**
- The use of `findPrefixOf` ensures that **all possible digit representations (including overlapping ones)** are detected at every position in the string, aligning with the problem's requirements.

---

## Why This Approach is Functional
- **No mutable state:** All data is transformed through expressions, not by changing variables.
- **No side effects:** Functions return values, not actions.
- **Composability:** Each transformation (splitting lines, extracting digits, summing) is a separate, reusable step.
- **Referential transparency:** The same input always produces the same output.

---

## Summary Table

| Concept             | Example in Code                           |
|---------------------|-------------------------------------------|
| Immutability        | `val stringDigitReprs = Map(...)`         |
| Pure Functions      | `def lineToCoordinates(line: String)`     |
| Higher-Order Funcs  | `.map(lineToCoordinates(_))`              |
| Declarative Style   | `.linesIterator.map(...).sum`             |
| Comprehensions      | `for lineTail <- line.tails ... yield ...`|
| No Side Effects     | No printing/mutation in computation       |

---

## Further Reading
- [Scala for Functional Programming](https://docs.scala-lang.org/tour/functional-programming.html)
- [Scala Collections](https://docs.scala-lang.org/overviews/collections/introduction.html)
- [Immutability and Pure Functions](https://docs.scala-lang.org/overviews/core/immutability.html)

