# =====================================================================
# ⏩ ORDER OF OPERATION IN PYTHON (OPERATOR PRECEDENCE)
# =====================================================================

# () Parentheses  → Highest priority → evaluated first
# ** Exponent (power)
# *, /, //, % → Multiplication & Division level
# +, - → Addition & Subtraction level
# <, >, <=, >= → Comparison operators
# ==, != → Equality operators
# is, is not → Identity operators
# and → True if BOTH are True
# or  → True if ANY ONE is True
# = Assignment  → evaluated last

# Example showing correct precedence:
result = 10 + 3 * 2 ** 2
print(result)  # 10 + 3*4 = 10 + 12 = 22


# =====================================================================
# 🔍 NUMBER DATATYPE BEHAVIOR
# =====================================================================

num01 = 55        # int
print(type(num01))

num02 = 55.55     # float
print(type(num02))

# Mixed-type arithmetic → Python auto-upgrades to higher precision
num03 = num01 + num02
print(num03, type(num03))  # float ✔

num04 = 55.55j    # complex number
print(type(num04))


# Multiple values grouped → Python creates a tuple
num05 = (num01, num02, num03, num04)
print(num05)

num06 = (3+2j)*6
print(num06)   # 18+12j

# Some important numeric operations
print(num01 % 25)   # modulus (remainder)
print(num01 // 14)  # integer division (floor result)
print(num01 ** 3)   # power → exponent

# =====================================================================
# 🛑 BAD vs GOOD Expression — Correct Precedence Use
# =====================================================================

# BAD ❌ — Hard to understand
print(num01 + num02 * num04)

# GOOD ✔ — Use parentheses to show intention clearly
print((num01 + num02) * num04)
print(num01 + (num02 * num04))


# =====================================================================
# 🔄 OPERATOR OVERLOADING — Python Flexibility
# =====================================================================

# + operator behaves differently based on datatype
print(5 + 5)       # 10 (numeric addition)
print("hello " + "python")  # string concat
print([1,2] + [3,4]) # list concat

# BUT mismatched types give error:
# print("name" + 5)  # ❌ TypeError

print(str(5) + "name")  # ✔ Best practice → explicit conversion


# =====================================================================
# 🧠 repr(), str(), print() — Difference Fully Explained
# =====================================================================

x = "Hello, World!"

print(repr(x))  # Developer friendly → shows quotes + escapes
# Output: "'Hello, World!'"

print(str(x))   # User friendly → readable output
# Output: Hello, World!

print(x)        # print() uses str() behind the scenes


# =====================================================================
# 🔢 BOOLEAN — Internal Numeric Behavior
# =====================================================================

print(True, False)
print(True + True)  # 1 + 1 = 2 ✔
print(False + True) # 0 + 1 = 1 ✔

# Valid comparisons using boolean
print(True == 1)  # True (same numeric value)
print(False == 0) # True

# But "is" checks memory → different types
print(True is 1)  # False


# =====================================================================
# 🔁 OPERATOR BEHAVIOR NOTES
# =====================================================================

# ==  → Checks VALUE equality
# =   → Assignment operator
# is  → Checks OBJECT ID (same memory reference)

# Good example:
a = 10
b = 10
print(a == b)  # True ✔ both values same
print(a is b)  # True ✔ both reference same (because small int cached)

# ❗Misconception fixed:
# == does NOT check datatype → it only checks value equality
print(5 == 5.0)  # True (int == float compares values)
print(type(5), type(5.0))  # Different types



# =====================================================================
# ⚠️ CHAINED COMPARISONS MUST BE USED CAREFULLY
# =====================================================================

# ❌ Bad practice (confusing)
print(1 < 2 < 3)

# ✔ Explicit & clear
print(1 < 2 and 2 < 3)

# ❌ Bad
print(1 == 2 < 3)  # false

# ✔ Good
print(1 == 2 and 2 < 3)


# =====================================================================
# 📌 CONDITIONAL DEMO
# =====================================================================

if 1 < 2 or 2 > 3:
    print("The condition is true")
