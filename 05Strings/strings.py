# =====================================================================
# 📝 STRINGS IN PYTHON —  NOTES
# =====================================================================

# ✔ Strings are IMMUTABLE sequences of characters in Python.
#   → Once created, the original string cannot be changed.
#   → Any modification creates a NEW string in memory.


# ---------------------------------------------------------------------
# 📌 String Declaration
# ---------------------------------------------------------------------
empty_string_01 = ""
empty_string_02 = ''
empty_string_03 = """"""  # Triple quotes can also define empty or multiline strings

username = "John Doe"
print(username)  # Output: John Doe


# ---------------------------------------------------------------------
# 📌 Accessing Characters using Indexing
# ---------------------------------------------------------------------
# Index always starts from 0 (left to right)
print(username[0])  # 'J'
print(username[1])  # 'o'

# Negative indexing → right to left (last char = -1)
print(username[-1])  # 'e'
print(username[-2])  # 'o'


# ---------------------------------------------------------------------
# 📌 String Slicing — Extracting Part of String
# Syntax: string[start:end:step]
# ---------------------------------------------------------------------
print(username[0:4])   # 'John'  → from index 0 to 3
print(username[:4])    # 'John'  → start omitted means 0
print(username[4:])    # 'Doe'   → until end
print(username[4:8])   # 'Doe'

# Advanced slicing with steps
num_string = "0123456789"
print(num_string[0:9:2])  # 02468  → every 2nd character
print(num_string[::2])    # 02468
print(num_string[::-1])   # Reverse string → 9876543210
print(num_string[:7:3])   # 036
print(num_string[1::3])   # 147


# ---------------------------------------------------------------------
# 📌 Useful String Built-in Methods
# ---------------------------------------------------------------------

# Length of string
print(len(username))  # 8 characters

# Find starting index of substring
print(username.index("Doe"))  # 5

# Count occurrences of a character
print(username.count("o"))  # 2

# Replace content → returns new string
print(username.replace("Doe", "Smith"))
# Original remains same because IMMUTABLE
print(username)

# Find substring → returns -1 if not found
print(username.find("Doe"))    # 5
print(username.find("Smith"))  # -1


# ---------------------------------------------------------------------
# 📌 Strip Method — Removes Leading & Trailing spaces
# ---------------------------------------------------------------------
name = "   Knight"
email = "♠example@email.com    "
password = "  123456  "

print(name.strip())
print(email.strip())
print(password.strip())


# ---------------------------------------------------------------------
# 📌 String Concatenation
# ---------------------------------------------------------------------
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)


# ---------------------------------------------------------------------
# 📌 String Formatting
# ---------------------------------------------------------------------
product = "Python"
count = "first"
statement = "Today we will try {} for the {} time"
print(statement.format(product, count))  # Fills {} in order

# ✔ Modern formatting (recommended)
print(f"Today we will try {product} for the {count} time")  # f-string


# ---------------------------------------------------------------------
# 📌 Raw Strings, Unicode & Escape Sequences
# ---------------------------------------------------------------------
str01 = "This is a string\nwith line break"
print(str01)  # \n creates a new line

# Escape characters require double backslashes
file_path_01 = "c:\\path\\to\\file.txt"
print(file_path_01)

# Raw String → treats backslashes as normal chars (No escape)
str02 = r"This is a string\nwith RAW string"
print(str02)

file_path_02 = r"c:\path\to\file.txt"
print(file_path_02)

# Quotes inside string
str03 = "He said \"Python is awesome\""
print(str03)

# Summary of Common Escape Sequences:
# \n → newline
# \t → tab
# \\ → backslash
# \' → single quote
# \" → double quote


# ---------------------------------------------------------------------
# 📌 Case Conversion
# ---------------------------------------------------------------------
username_01 = "John Doe"
print(username_01.upper())  # JOHN DOE

username_02 = "John Doe"
print(username_02.lower())  # john doe


# ---------------------------------------------------------------------
# 📌 Splitting Strings → Convert to List
# ---------------------------------------------------------------------
myString = "Apple, Samsung, Google"
print(myString.split(", "))  # ['Apple','Samsung','Google']


# ---------------------------------------------------------------------
# 📌 Joining List into String
# ---------------------------------------------------------------------
myList = ["Apple", "Samsung", "Google"]
print(", ".join(myList))  # Apple, Samsung, Google


# ---------------------------------------------------------------------
# 📌 Iterating Over String
# ---------------------------------------------------------------------
for elements in username:
    print(elements)


# ---------------------------------------------------------------------
# 📌 Membership Test in String → 'in' Operator
# ---------------------------------------------------------------------
print("Doe" in username)    # True
print("Smith" in username)  # False


# ---------------------------------------------------------------------
# 🎯 Final Interview Notes
# ---------------------------------------------------------------------
# ✔ String = Ordered + Immutable + Iterable
# ✔ Supports indexing, slicing and looping
# ✔ Most operations return NEW string (because immutable)
# ✔ strip(), split(), join(), replace(), find() etc. are most used
# ✔ f-strings are best for formatting
# ✔ Raw strings useful for file paths and regex
# ✔ Python strings support Unicode (multi-language)
# =====================================================================
