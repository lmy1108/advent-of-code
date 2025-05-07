# Regex Cheatsheet: 10 Most Useful Patterns

This guide lists 10 of the most versatile and commonly used regex patterns, with examples and explanations. At the end, you'll find 10 common regex mistakes and misunderstandings.

---

## 1. Match a Number (Integer)
- **Regex:** `\d+`
- **Example:** `"abc123def"` → matches `123`
- **Explanation:** `\d` matches any digit; `+` means one or more.

---

## 2. Match a Floating Point Number
- **Regex:** `[-+]?\d*\.\d+`
- **Example:** `"pi=3.1415, -2.0"` → matches `3.1415`, `-2.0`
- **Explanation:** Optional sign, digits, a dot, and more digits.

---

## 3. Match a Word (Letters, Digits, Underscore)
- **Regex:** `\w+`
- **Example:** `"foo_bar123"` → matches `foo_bar123`
- **Explanation:** `\w` matches [a-zA-Z0-9_]; `+` for one or more.

---

## 4. Match an Email Address (Simple)
- **Regex:** `[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}`
- **Example:** `"contact: john.doe@mail.com"` → matches `john.doe@mail.com`
- **Explanation:** User, `@`, domain, dot, TLD.

---

## 5. Match a Date (YYYY-MM-DD)
- **Regex:** `\b\d{4}-\d{2}-\d{2}\b`
- **Example:** `"Today is 2024-05-06."` → matches `2024-05-06`
- **Explanation:** Four digits, dash, two digits, dash, two digits, word boundaries.

---

## 6. Match a URL (Simple)
- **Regex:** `https?://[^\s]+`
- **Example:** `"Visit https://example.com/page"` → matches `https://example.com/page`
- **Explanation:** `http` or `https`, `://`, then non-whitespace.

---

## 7. Match Anything in Quotes
- **Regex:** `"(.*?)"`
- **Example:** `He said, "hello world".` → matches `"hello world"`
- **Explanation:** Double quotes, minimal match inside.

---

## 8. Match a US Phone Number
- **Regex:** `\(\d{3}\) \d{3}-\d{4}`
- **Example:** `"Call (123) 456-7890"` → matches `(123) 456-7890`
- **Explanation:** (Area code) space, three digits, dash, four digits.

---

## 9. Match a Hex Color Code
- **Regex:** `#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b`
- **Example:** `"Color: #ff0033 or #abc"` → matches `#ff0033`, `#abc`
- **Explanation:** `#` followed by 3 or 6 hex digits.

---

## 10. Match Start and End of Line
- **Regex:** `^start.*end$`
- **Example:** `"start here and end"` → matches whole line if it starts with `start` and ends with `end`.
- **Explanation:** `^` anchors to line start, `$` to line end.

---

# 10 Common Regex Mistakes & Pitfalls

1. **Greedy Matching:** Using `.*` instead of `.*?` can over-consume text.
2. **Forgetting to Escape Special Characters:** E.g. `.` matches any character, not a literal dot. Use `\.`.
3. **Anchors Misuse:** `^` and `$` are line-based, not string-based unless in multiline mode.
4. **Not Using Raw Strings in Python:** Always use `r"..."` to avoid double escaping.
5. **Confusing `+` and `*`:** `+` is one or more, `*` is zero or more.
6. **Not Specifying Word Boundaries:** Without `\b`, partial matches (e.g. `cat` in `scatter`).
7. **Forgetting Grouping Parentheses:** Needed for extracting submatches.
8. **Overusing Character Classes:** `[a-zA-Z0-9_]` is just `\w`.
9. **Not Handling Newlines:** `.` does not match newlines unless you use `re.DOTALL`.
10. **Backreference Confusion:** Using `\1`, `\2` incorrectly or forgetting to group.

---

**Tip:** Use online tools like [regex101.com](https://regex101.com/) to experiment and debug your regexes interactively.
