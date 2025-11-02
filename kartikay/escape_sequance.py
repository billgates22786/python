# Escape Sequences in Python

# \n – Newline (line break)
print("This is line 1\nThis is line 2")

# \t – Horizontal tab
print("Column 1\tColumn 2")

# \r – Carriage return (moves cursor to the start of the line)
print("Hello World\rStart")

# \b – Backspace (deletes the previous character)
print("Hello\b World")

# \f – Form feed (advances to the next "page" in the text output, often used in printers)
print("Page 1\fPage 2")

# \' – Single quote
print('It\'s a sunny day')

# \" – Double quote
print("She said, \"Hello!\"")

# \\ – Backslash
print("This is a backslash: \\")

# \v – Vertical tab (advances to the next vertical tab stop, often not visible)
print("Vertical\vTab")

# \a – Bell/Alert (produces a sound alert in the terminal, if supported)
print("Bell sound\a")

# \0 – Null character (a non-visible character)
print("This is a null character\0 in between")

# \ooo – Character with octal value ooo
print("Octal value character: \141")  # \141 represents 'a' in octal

# \xhh – Character with hexadecimal value hh
print("Hexadecimal value character: \x61")  # \x61 represents 'a' in hexadecimal

# \N{name} – Unicode character by its name
print("Unicode character by name: \N{GREEK CAPITAL LETTER DELTA}")  # Δ

# \uXXXX – Unicode character with a 16-bit hex value
print("16-bit Unicode: \u03A9")  # Ω (Greek capital letter Omega)

# \UXXXXXXXX – Unicode character with a 32-bit hex value
print("32-bit Unicode: \U0001F600")  # 😀 (grinning face emoji)
