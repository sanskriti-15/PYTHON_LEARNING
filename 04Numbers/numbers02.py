# 🧮 OPERATOR PRECEDENCE (VERY IMPORTANT)
# =====================================================================
# ORDER OF EXECUTION (Top → Highest Priority)
#
# 1️⃣ ()      → Parentheses
# 2️⃣ **      → Exponent (Power)
# 3️⃣ *, /, //, % → Multiplication, Division, Floor, Modulus
# 4️⃣ +, -    → Addition, Subtraction
# 5️⃣ <, >, <=, >=, ==, != → Comparisons
# 6️⃣ is, is not → Identity check (memory reference)
# 7️⃣ and     → Logical AND
# 8️⃣ or      → Logical OR
# 9️⃣ =       → Assignment (lowest priority)
#
# ✔ ALWAYS use parentheses in complex expressions for clarity

# =====================================================================
# 8️⃣ OCTAL, HEXADECIMAL & BINARY NUMBERS — Storage Formats
# =====================================================================

# ➝ We can write numbers in different numeric bases

# Octal → Base-8 → digits: 0-7
print(0o10)  # 8
print(0o20)  # 16

# Hexadecimal → Base-16 → digits: 0-9 + A-F
print(0x10)  # 16
print(0x20)  # 32

# Binary → Base-2 → digits: 0,1
print(0b1000)  # 8
print(0b1100)  # 12

# =====================================================================
# 🔁 NUMBER BASE CONVERSION (Built-in Methods)
# =====================================================================

print(bin(10))  # → Convert to binary:   0b1010
print(oct(64))  # → Convert to octal:    0o100
print(hex(255)) # → Convert to hex:      0xff

# =====================================================================
# ⚙️ BITWISE OPERATORS — Work on bits (Binary digits)
# =====================================================================

x = 5  # → binary: 0101
y = 3  # → binary: 0011

print(x & y)  # AND  → 0001 = 1
print(x | y)  # OR   → 0111 = 7
print(x ^ y)  # XOR  → 0110 = 6
print(~x)     # NOT  → -(x+1) = -6 (2's complement)

print(x << 2) # Left shift  = 20 → 0101 << 2 => 010100
print(x >> 1) # Right shift = 2  → drop last bit

# =====================================================================
# ⚠️ FLOATING-POINT PROBLEM — Internal Binary Rounding
# =====================================================================

print(0.1 + 0.2)              # 0.30000000000000004
print(0.1 + 0.1 + 0.1 - 0.3)  # tiny floating error

# ❓ Why?
# Because 0.1 cannot be represented EXACTLY in binary

# ✔ SOLUTION → use Decimal for precision
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
# Output: 0  → CORRECT ✔

# =====================================================================
# ➗ FRACTIONS — Exact Rational Arithmetic (No precision loss)
# =====================================================================

from fractions import Fraction
print(Fraction(1, 3))  # → 1/3 exactly ✔

# =====================================================================
# 🔷 SET DATA TYPE — Unique & Unordered Collection
# =====================================================================

mySet = {1, 2, 3, 4, 5}
print(mySet)

# ✔ Set operations (Very fast for membership)
print(mySet & {2, 3, 4, 5})  # Intersection → {2,3,4,5}
print(mySet | {2, 3, 4, 5})  # Union → {1,2,3,4,5}
print(mySet - {2, 3, 4, 5})  # Difference → {1,5}
print(mySet ^ {2, 3, 4, 5})  # Symmetric diff → {1,5}

# ✔ Subset / Superset checking:
print(mySet <= {1,2,3,4,5})  # True → mySet is subset
print(mySet >= {1,2,3,4,5})  # True → mySet is superset

# ✔ Empty curly braces {} is NOT a set → it is a dictionary
print(type({}))  # <class 'dict'>
print