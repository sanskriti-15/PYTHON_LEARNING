# =====================================================================
# INTERNAL WORKING OF VARIABLES IN PYTHON — VERY IMPORTANT CONCEPTS
# =====================================================================


# ✔ Variables DO NOT store values in Python
# ✔ Variables ONLY store references (pointers) to objects in memory
# ✔ Data type belongs to the OBJECT, not the variable


# ---------------------------------------------------------------------
# Example 1️⃣ : Immutable Object (int)
# ---------------------------------------------------------------------
x = 10

# MEMORY VISUAL:
# +----------------+
# |   10 (int)     |
# +----------------+
#        ▲
#        |
#        x   ← x is pointing to the object 10

# ✔ "10" lives in memory
# ✔ "x" is just a label pointing to that memory location
# ✔ Variable does NOT contain the value itself


# ---------------------------------------------------------------------
# Example 2️⃣ : Changing value of Immutable
# ---------------------------------------------------------------------
y = x   # y points to the SAME object as x

# BEFORE CHANGE:
# x ──┐
#     ▼
#   +------+
#   |  10  |
#   +------+
#      ▲
#      |
#      y  ← Same reference

x = 20  # new integer created → NEW memory

# AFTER CHANGE:
# x → +------+
#     |  20  |
#     +------+
#
# y → +------+
#     |  10  |
#     +------+

# ✔ Immutable → New object created on modification
# ✔ "y" still points to old value 10


# ---------------------------------------------------------------------
# Example 3️⃣ : Mutable Object (list)
# ---------------------------------------------------------------------
L1 = [1, 2, 3]
L2 = L1

# MEMORY VISUAL:
# +----------------+
# | [1, 2, 3] list |
# +----------------+
#      ▲     ▲
#      |     |
#     L1    L2   ← Both point to SAME object in memory

L1[0] = 99   # modify list element

# SAME memory updated → change visible via both names:
# L1 → [99, 2, 3]
# L2 → [99, 2, 3]

# ✔ Mutable → No new memory created
# ✔ All variables pointing to it see the change


l1 =[11,22,33]
l2 = l1
l1 = [11,22,33]
l1[0]=999

# MEMORY VISUAL:
# +----------------+
# | [11, 22, 33] list |
# +----------------+
#      ▲     ▲
#      |     |
#     L1    L2   ← Both point to SAME object in memory



# +----------------+
# | [11, 22, 33] list |
# +----------------+
#          ▲
#          |
#          L2   ← l2 is pointing to same  object in memory


# +----------------+
# | [11, 22, 33] list |
# +----------------+
#      ▲     
#      |     
#     L1      ← l1 is pointing to DIFF object in memory

#  so now l1 is changes but l2 will not change


h1 = [1,2,3]

h2 = h1[:]
# h2 is a copy of h1
# now both h1 and h2 are poiting to diffrent memory location 

# ---------------------------------------------------------------------
# 🧠 WHY THIS MATTERS?
# ---------------------------------------------------------------------
# • Same object shared between variables → memory efficient
# • Can cause unexpected changes with mutable types
# • Must understand difference in behavior


# ---------------------------------------------------------------------
# ✔ FINAL SUMMARY (IMPORTANT FOR INTERVIEW)
# ---------------------------------------------------------------------
# VARIABLE:
#   • Just a name / label
#   • Stores reference to a memory location

# OBJECT:
#   • Real value stored in memory
#   • Has an actual data type (int, list, str, etc.)

# IMMUTABLE OBJECTS (int, str, tuple…)
#   • New object created when modified
#   • Reference changes

# MUTABLE OBJECTS (list, dict, set…)
#   • Update happens inside same memory location
#   • Reference remains same


# 🔥 Golden Line:
#    "Variables are just pointers. Objects store the actual data."
# =====================================================================


# =====================================================================
# 🔒 IMMUTABLE vs 🔓 MUTABLE — MEMORY BEHAVIOR
# =====================================================================

# 🧱 IMMUTABLE OBJECTS:
# • int, float, bool, str, tuple, bytes
# • Any change creates a NEW object in memory

num1 = 5
print(id(num1))     # Memory location 1
num1 = num1 + 2
print(id(num1))     # Memory location 2 → NEW object created ✔


# 🧩 MUTABLE OBJECTS:
# • list, dict, set, bytearray
# • Change happens inside SAME object in memory

L1 = [1, 2, 3]
print(id(L1))
L1.append(4)
print(id(L1))       # SAME memory → Mutable ✔


# =====================================================================
# 🧹 GARBAGE COLLECTION + REFERENCE COUNTING 📊 (FULL EXPLANATION)
# =====================================================================

# ✔ Python manages memory automatically using:
#   1️⃣ Reference Counting  → primary method
#   2️⃣ Garbage Collector   → backup for cyclic objects


import sys

# sys.getrefcount(object)
# This function returns: ➝ How many variables are currently pointing to this object

print(sys.getrefcount(24601))  # Example integer
print(sys.getrefcount(1))      # Small commonly used integer
print(sys.getrefcount('a'))    # Very frequently used string
print(sys.getrefcount('apple'))# Less commonly used string


# 📌 How does this work?

# Whenever a Python object is created,
# Python keeps track of HOW MANY REFERENCES are pointing to it.

# Example:
x = 5   # → refcount(5) = 1  (because x is pointing to it)
y = x   # → refcount(5) = 2  (x and y both point to 5)


# 🗑 When does an object get removed (garbage collected)?

# When the reference count becomes 0:
#   → No variable is pointing to that object anymore
#   → Object is deleted from memory automatically


# =====================================================================
# 🧠 Why does sys.getrefcount(1) or sys.getrefcount('a') show big numbers?
# =====================================================================

# ✔ Python performs an optimization called "INTERING"
# ✔ Frequently used values are kept ready in memory BEFORE PROGRAM RUNS
#   Example:
#       Small integers: -5 to 256
#       Common short strings: 'a', 'hello', ...
#
# Reason:
#   → Faster performance
#   → Saves memory by reusing the same object instead of creating new ones


# Example:
# All of these point to the SAME 'a' object in memory:
char1 = 'a'
char2 = 'a'
char3 = 'a'
# So refcount('a') becomes high!


# =====================================================================
# 🎯 Final Takeaway
# =====================================================================

# ✔ Python tracks how many variables refer to a value (reference count)
# ✔ When count becomes 0 → Memory is freed automatically (Garbage Collection)
# ✔ Small integers & common strings are INTERNED:
#     They may NEVER reach zero reference count while Python is running

# In simple words:
#  ➝ Python is smart enough to reuse common objects
#  ➝ and delete unused objects to save memory efficiently
# =====================================================================


# =====================================================================
# 🪞 SHALLOW COPY vs 🧬 DEEP COPY
# =====================================================================

import copy

myList01 = [1, 2, 3, 4]
myList02 = copy.copy(myList01)   # Shallow Copy
print(myList01, myList02)

myList03 = myList01[:]           # Another shallow copy way ✔
print(myList03)

myList04 = [1, 2, [3, 4], 5, "6"]
myList05 = copy.deepcopy(myList04)  # Deep Copy → duplicates nested list too
print(myList05)

# ❗ Shallow Copy Warning:
# If nested objects exist → changes reflect everywhere


# =====================================================================
# ⚖️ "==" vs "is" — TOP INTERVIEW QUESTION
# =====================================================================

myList01 = [1, 2, 3, 4]
myList02 = myList01
print(myList01 == myList02)  # True → Values equal
print(myList01 is myList02)  # True → SAME object ✔

myList03 = [1, 2, 3, 4]
myList04 = myList03[:]
print(myList03 == myList04)  # True → Values equal
print(myList03 is myList04)  # False → Different object ✔


# =====================================================================
# 🔄 MUTABLE REFERENCES — Multiple Names, Same Object
# =====================================================================

L1 = [1, 2, 3, 4]
L2 = L1
L1[0] = 55
print(L1, L2)   # BOTH changed → Same memory referenced

L3 = L2
L3[1] = 33
print("L2:", L2)
print("L3:", L3)
# ✔ Any modification reflects everywhere because SAME object


# =====================================================================
# ✂️ STRING vs LIST — Why Different?
# =====================================================================

username = "John Doe"
print(username[0:4])  # NEW string created → Immutable behavior

myList01 = [1, 2, 3, 4]
print(myList01[0:2])  # NEW list created → shallow copy


# =====================================================================
# ⚙️ PYTHON OPTIMIZATIONS — INTERNAL MAGIC ✨
# =====================================================================

# ✔ Small ints (-5 to 256) reused from memory pool
# ✔ Frequent strings (like 'a', 'hello') INTERNED
# ✔ Garbage collector runs when needed (not immediately)
# ✔ Reference counting controls object life
# ✔ Heavy math uses external libs (NumPy → GPU support)


# =====================================================================
# 🎯 FINAL INTERVIEW TAKEAWAYS
# =====================================================================

# ✔ Variables = References (pointers)
# ✔ Data types exist with the OBJECT → not variable
# ✔ Mutable → Modify in same memory
# ✔ Immutable → Create new object on change
# ✔ "==" = Value equality
# ✔ "is" = Identity / Memory equality
# ✔ Shallow copy → Dangerous for nested objects
# ✔ Deep copy → Safe for nested objects
# ✔ Python optimizes performance using interning
# ✔ Memory auto-cleaned using Garbage Collector

# =====================================================================

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
# STRING vs LIST MEMORY DIFFERENCE — EXPLANATION
# =====================================================================

username = "John Doe"
print(username[0:4])  

# ✔ Strings are IMMUTABLE in Python
# → Even slicing creates an entirely NEW STRING object
# → All characters are copied because strings cannot be modified


myList01 = [1, 2, 3, 4]
myList02 = myList01[0:2]
print(myList01 is myList02)

# ✔ Lists are MUTABLE in Python
# → Slicing ALSO creates a NEW LIST object
# BUT inside the list, elements are REFERENCED, not deep copied


# =====================================================================
# 🔍 Key Difference
# =====================================================================

# STRING SLICING:
#   • Returns a new string
#   • Since string chars are immutable → completely independent copy
#   • No internal structure → nothing shared

# LIST SLICING:
#   • Returns a new list object ✔
#   • BUT inner objects are NOT copied → only references copied
#     (This is called SHALLOW COPY)

# Visual:
# myList01: [1, 2, 3, 4]
# myList02: [1, 2]   # NEW list, but elements point to SAME integer objects inside memory


# =====================================================================
# 🧠 Example Showing Behavior Difference
# =====================================================================

# ✔ Immutable elements like integers → appear independent
#   because modifying element creates NEW object

myList02[0] = 99
print(myList01)   # Still [1, 2, 3, 4] → no effect
print(myList02)   # [99, 2]


# BUT for nested mutable elements 👇

nested = [[1, 2], [3, 4]]
shallow = nested[:]
shallow[0][0] = 999

print(nested)   # [[999, 2], [3, 4]] → inner list changed!
print(shallow)  # SAME → because they share INNER objects


# =====================================================================
# 🎯 Conclusion
# =====================================================================

# Both slicing operations create NEW objects:
#   username[0:4] → NEW STRING ✔
#   myList01[0:2] → NEW LIST ✔

# Difference:
#   String slicing → FULLY independent copy (immutable)
#   List slicing → NEW container but internal elements still shared (mutable)

# In simple words:
#   Strings → Copy everything (safe)
#   Lists → Copy only container, not contents (shallow)
# =====================================================================


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
