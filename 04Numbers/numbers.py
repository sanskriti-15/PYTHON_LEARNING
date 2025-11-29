# =====================================================================
# 🧠 BOOLEAN DATA TYPE — LINKED WITH NUMBERS
# =====================================================================

# ✔ True behaves like 1
# ✔ False behaves like 0
# ✔ Boolean is a wrapper over integers (subclass of int)

print(1 == 1)   # True  → 1
print(1 == 2)   # False → 0

print(True + True)   # 1 + 1 = 2
print(False + False) # 0 + 0 = 0

print(type(True))    # <class 'bool'>

print(True == 1)     # True  → same numeric value
print(False == 0)    # True

print(True is 1)     # False → different identity (memory reference)

# ✔ Recommendation:
# Avoid math with True/False, it looks confusing
print(True + 4)  # Output: 5  (not recommended)

# =====================================================================
# 🪞 repr(), str(), print() — FULL COMMENT EXPLANATION
# =====================================================================

x = 'Hello, World!'

# repr() → Developer view: unambiguous, shows quotes, escape chars
print(repr(x))  
# Output: "'Hello, World!'"

# str() → User-friendly readable view
print(str(x))   
# Output: Hello, World!

# print() → Displays using str() internally
print(x)       
# Output: Hello, World!

# ✔ repr() helps debugging
# ✔ str() helps clean user output

# =====================================================================
# 📦 IMPORTING MATH MODULE — IMPORTANT NUMBER FUNCTIONS
# =====================================================================

import math

# floor() → Round down to nearest number
print(math.floor(5.55))   # 5
print(math.floor(-5.55))  # -6 (moves downwards)

# trunc() → Remove decimals → moves toward zero
print(math.trunc(-5.55))  # -5

# ceil() → Round up to nearest number
print(math.ceil(5.55))    # 6

# Predefined mathematical constants
print(math.pi)
print(math.e)

# Square root
print(math.sqrt(25))

# Power
print(math.pow(2, 3))  # Result is float always

# Factorial
print(math.factorial(5))  # 120

# =====================================================================
# 🎲 RANDOM MODULE — RANDOM NUMBERS & SHUFFLING
# =====================================================================

import random

numList = ["A", "B", "C", "D", "E"]
print(numList)

print(random.random())   # Random float: 0 to 1
print(random.randint(1, 10))  # Random int: 1 to 10
print(random.choice(numList)) # Random item from list

random.shuffle(numList)  # Shuffle list order
print(numList)

# ✔ random module mainly used in:
#   • simulations
#   • games
#   • data sampling
#   • AI training