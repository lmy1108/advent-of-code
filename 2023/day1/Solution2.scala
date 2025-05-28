import scala.io.Source

@main def part2: Unit =
  // Read the entire input file as a single string
  val input = Source.fromFile("input.txt").mkString
  // Print the computed solution
  println(s"The solution is ${part2(input)}")

// Map of number words to their digit values
val stringDigitReprs = Map(
  "one" -> 1,
  "two" -> 2,
  "three" -> 3,
  "four" -> 4,
  "five" -> 5,
  "six" -> 6,
  "seven" -> 7,
  "eight" -> 8,
  "nine" -> 9,
)
// Map of all digit representations (number words and digit characters)
val digitReprs = stringDigitReprs ++ (1 to 9).map(i => i.toString() -> i)

def part2(input: String): String =
  // Regex that matches any digit representation (word or digit character)
  val digitReprRegex = digitReprs.keysIterator.mkString("|").r

  // Extracts the calibration value from a line
  def lineToCoordinates(line: String): Int =
    // For every suffix of the line, find all digit representations that match as a prefix
    val matchesIter =
      for
        lineTail <- line.tails
        oneMatch <- digitReprRegex.findPrefixOf(lineTail)
      yield
        oneMatch
    val matches = matchesIter.toList
    // If no matches, return 0 for this line
    if (matches.isEmpty) 0
    else {
      // Convert the first and last match to their digit values and form the calibration number
      val firstDigit = digitReprs(matches.head)
      val lastDigit = digitReprs(matches.last)
      s"$firstDigit$lastDigit".toInt
    }
  end lineToCoordinates

  // Process each line, extract its calibration value, and sum all values
  val result = input
    .linesIterator
    .map(lineToCoordinates(_))
    .sum
  result.toString()
end part2