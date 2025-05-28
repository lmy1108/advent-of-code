# Useful Vim Navigation Commands

Here are essential Vim commands for moving the cursor and editing efficiently, especially for start/end of line, non-blank, and word navigation.

## Moving Within a Line
| Command    | Action                                              |
|------------|-----------------------------------------------------|
| `0`        | Move to the start of the line (column 0)            |
| `^`        | Move to the first non-blank character of the line   |
| `$`        | Move to the end of the line                         |
| `g_`       | Move to the last non-blank character of the line    |
| `w`        | Move forward to the start of the next word          |
| `b`        | Move backward to the start of the previous word     |
| `e`        | Move to the end of the current/next word            |
| `f<char>`  | Move forward to the next occurrence of `<char>`     |
| `F<char>`  | Move backward to the previous occurrence of `<char>`|
| `t<char>`  | Move forward up to (before) next `<char>`           |
| `T<char>`  | Move backward up to (before) previous `<char>`      |

## Editing at Start/End of Line or Word
| Command | Action                                                          |
|---------|-----------------------------------------------------------------|
| `A`     | Move to end of line and enter insert mode (append)              |
| `I`     | Move to first non-blank character and enter insert mode         |
| `0i`    | Move to column 0 and enter insert mode (rarely needed)          |
| `O`     | Open new line above and enter insert mode                       |
| `o`     | Open new line below and enter insert mode                       |
| `b`+`i` | Move to start of word, then insert mode (at word start)         |
| `e`+`a` | Move to end of word, then insert mode after (after word end)    |

## Summary Table: Editing at Logical Positions
| Goal                                   | Command(s)   | Description                         |
|----------------------------------------|--------------|-------------------------------------|
| Insert at start of line (non-blank)    | `I`          | First non-blank char, insert mode   |
| Insert at end of line                  | `A`          | End of line, insert mode            |
| Insert at absolute start (col 0)       | `0i`         | Column 0, insert mode               |
| Insert at start of current word        | `b` then `i` | Move to word start, insert mode     |
| Insert after end of current word       | `e` then `a` | Move to word end, insert after      |
| Open new line above                    | `O`          | New line above, insert mode         |
| Open new line below                    | `o`          | New line below, insert mode         |

## Other Useful Navigation Commands
| Command    | Action                                              |
|------------|-----------------------------------------------------|
| `gg`       | Go to the first line of the file                     |
| `G`        | Go to the last line of the file                      |
| `:n`       | Go to line number `n`                                |
| `H`        | Move to the top of the screen                        |
| `M`        | Move to the middle of the screen                     |
| `L`        | Move to the bottom of the screen                     |

## Visual Mode Movement
| Command    | Action                                              |
|------------|-----------------------------------------------------|
| `v`        | Start visual mode (characterwise selection)          |
| `V`        | Start visual line mode                               |
| `Ctrl+v`   | Start visual block mode                              |

---

## Examples
- Press `0` to jump to the start of the current line.
- Press `^` to jump to the first non-blank character.
- Press `$` to jump to the end of the current line.
- Press `f,` to jump to the next comma on the line.
- Press `gg` to go to the first line of the file.
- Press `I` to insert at the first non-blank character.
- Press `A` to insert at the end of the line.
- Press `b` then `i` to insert at the start of the current word.
- Press `e` then `a` to insert after the end of the current word.

---

For more, see `:help motion` in Vim or visit [Vim documentation](https://vimhelp.org/).
