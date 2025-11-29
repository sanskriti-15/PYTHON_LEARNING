# =====================================================================
# INTERNAL WORKING OF VARIABLES IN PYTHON — VERY IMPORTANT CONCEPTS
# =====================================================================

# ✔ In Python, variables DO NOT store values directly
# ✔ Variables only store a REFERENCE to a value stored in memory
# ✔ The REAL data type exists inside memory, NOT with variable

# Example:
x = 10
# Here:
# • 10 is stored in memory as an integer object
# • x is just a reference (pointer) to that memory location

# That’s why in Python:
#     Variables have NO fixed type
#     But objects inside memory DO have type

# =====================================================================
# IMMUTABLE vs MUTABLE INTERNAL WORKING
# =====================================================================

# ✔ IMMUTABLE OBJECTS (int, float, bool, str, tuple, bytes)
#   → CANNOT be changed in-place
#   → New value = NEW memory object created
#   → Old value reference removed (Garbage Collector will clean later)

num1 = 5
print(id(num1))
num1 = num1 + 2   # new integer created
print(id(num1))   # memory address changed → Immutable behavior


# ✔ MUTABLE OBJECTS (list, dict, set, bytearray)
#   → Can be updated inside same memory location
L1 = [1, 2, 3]
print(id(L1))
L1.append(4)      # modifies memory, no new object created
print(id(L1))     # SAME address → Mutable behavior


# =====================================================================
# PYTHON GARBAGE COLLECTION & REFERENCE COUNTING
# =====================================================================
# Python counts number of references pointing to a value.
# When count becomes ZERO → Object is deleted automatically

import sys
print(sys.getrefcount(24601))
print(sys.getrefcount(1))
print(sys.getrefcount('a'))
print(sys.getrefcount('apple'))
# NOTE: Values like 1, small strings, and common objects are INTERNED
#       Python keeps them alive for performance optimization.


# =====================================================================
# SHALLOW COPY vs DEEP COPY
# =====================================================================
import copy

myList01 = [1, 2, 3, 4]
myList02 = copy.copy(myList01)  # SHALLOW COPY — new list but same inner refs
print(myList01, myList02)

myList03 = myList01[:]          # Another shallow copy (via slicing)
print(myList03)

myList04 = [1, 2, [3, 4], 5, "6"]
myList05 = copy.deepcopy(myList04) # DEEP COPY — duplicates inner list too
print(myList05)

# ❗Shallow Copy Problem:
# Changing nested list inside myList04 will also affect myList02 and myList03
# Deep Copy prevents this.


# =====================================================================
# "is" vs "==" — VERY IMPORTANT DIFFERENCE
# =====================================================================

# == compares VALUES
# is compares MEMORY LOCATION (reference)

myList01 = [1, 2, 3, 4]
myList02 = myList01
print(myList01 == myList02)  # True → same value
print(myList01 is myList02)  # True → same memory (same object)

myList03 = [1, 2, 3, 4]
myList04 = myList03[:]
print(myList03 == myList04)  # True → same value
print(myList03 is myList04)  # False → different memory

myList05 = [1, 2, 3, 4]
myList06 = list(myList05)
print(myList05 == myList06)  # True
print(myList05 is myList06)  # False


# =====================================================================
# INTERNAL MEMORY BEHAVIOR — Mutable Object References
# =====================================================================
L1 = [1, 2, 3, 4]
L2 = L1  # both refer SAME memory
L1[0] = 55
print(L1, L2)  # both changed → SAME MEMORY


L3 = L2
L3[1] = 33
print("The L2 value is: ", L2)
print("The L3 value is: ", L3)
# Changes via one reference affect all variables pointing there
# Because MUTABLE VALUES allow in-place modification


# =====================================================================
# STRING vs LIST MEMORY DIFFERENCE
# =====================================================================
username = "John Doe"
print(username[0:4])  # slicing returns NEW string → immutable behavior

myList01 = [1, 2, 3, 4]
print(myList01[0:2])  # slicing returns NEW list → shallow copy


# =====================================================================
# PYTHON COMPILER OPTIMIZATION NOTES
# =====================================================================

# ✔ Python reuses memory for small integers (-5 to 256)
# ✔ Python interns commonly used strings ("a", "hello", etc.)
#   → Faster performance
# ✔ Garbage collection does NOT run immediately
# ✔ Reference count controls life of objects
# ✔ CPU/GPU computation depends on imported libraries like NumPy


# =====================================================================
# FINAL INTERVIEW TAKEAWAYS
# =====================================================================
# ✔ Variables store references, not the actual values
# ✔ Mutable = changes inside original memory
# ✔ Immutable = new object created for every modification
# ✔ "==" checks value equality
# ✔ "is" checks memory identity
# ✔ Shallow copy shares internal objects → risky for nested collections
# ✔ Deep copy duplicates everything → safe for nested objects
# ✔ Python optimizes numbers & strings using interning
# ✔ Garbage collector removes unreferenced memory objects automatically
