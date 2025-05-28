# File Reading in Scala: Using `Source`

This document explains how file reading works in Scala, with a focus on the usage of `Source.fromFile`, as seen in the snippet:

```scala
import scala.io.Source
val input = Source.fromFile("input.txt").mkString
```

---

## 1. The `Source` Object
- The `Source` object is part of the `scala.io` package.
- It provides convenient methods for reading data from files, URLs, strings, and other sources.

## 2. Reading a File
- `Source.fromFile("input.txt")` creates a `BufferedSource` that represents the contents of `input.txt`.
- This object can be iterated over line by line, character by character, or read all at once.

### Common Methods
- `.getLines`: Returns an iterator over the lines in the file (lazy, does not load the whole file into memory).
- `.mkString`: Reads the entire contents of the file into a single string (eager, loads the whole file).
- `.foreach`, `.map`: Can be used to process lines or characters.

### Example Usages
#### Read Entire File as String
```scala
val input = Source.fromFile("input.txt").mkString
```

#### Read File Line by Line
```scala
val lines = Source.fromFile("input.txt").getLines
for (line <- lines) {
  println(line)
}
```

#### Read File into a List of Strings (lines)
```scala
val linesList = Source.fromFile("input.txt").getLines.toList
```

---

## 3. Closing the Source
- When you use `Source.fromFile`, it's good practice to close the source after reading to free system resources.
- If you use `.mkString` or `.getLines.toList`, you can close the source immediately after reading:

```scala
val source = Source.fromFile("input.txt")
val input = source.mkString
source.close()
```

- In short scripts, not closing the source is usually not a big problem, but in larger applications it's recommended.

---

## 4. Error Handling
- If the file does not exist or cannot be read, `Source.fromFile` will throw an exception (e.g., `FileNotFoundException`).
- You can handle this with try/catch if needed.

---

## 5. Summary Table
| Usage                        | Description                           |
|------------------------------|---------------------------------------|
| `Source.fromFile(f)`         | Open file for reading                 |
| `.mkString`                  | Read entire file as one string        |
| `.getLines`                  | Iterator over lines (lazy)            |
| `.getLines.toList`           | List of lines (eager)                 |
| `.close()`                   | Close the file                        |

---

## 6. Further Reading
- [Scala Standard Library Docs: scala.io.Source](https://www.scala-lang.org/api/current/scala/io/Source$.html)
- [Scala Cookbook: Reading Files](https://docs.scala-lang.org/overviews/scala-book/reading-and-writing-files.html)
