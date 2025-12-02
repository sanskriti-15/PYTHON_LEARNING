# =====================================================================
# 🟣 TUPLE — IMMUTABLE & ORDERED SEQUENCE DATA TYPE
# =====================================================================
# ✔ Stores multiple values like list but IMMUTABLE (cannot be changed)
# ✔ Faster and uses less memory than list → more performance friendly
# ✔ Useful for FIXED data (e.g., coordinates, constants)
# ✔ Duplicate elements allowed
# ✔ Index based access
# =====================================================================

myTuple01 = (0,1,2,3,4,5,6,7,8,9)
print(myTuple01)

# Accessing tuple elements (indexing)
print(myTuple01[0])  # 0
print(myTuple01[1])  # 1
print(myTuple01[-1]) # 9 → last element
print(myTuple01[-2]) # 8 → second last


# ---------------------------------------------------------------------
# 🟡 TUPLE SLICING (Similar to Lists)
# ---------------------------------------------------------------------
print(myTuple01[0:2])  # (0, 1)
print(myTuple01[:3])   # (0, 1, 2)
print(myTuple01[3:])   # (3, 4, 5, 6, 7, 8, 9)


# ---------------------------------------------------------------------
# 🟣 TUPLE CONCATENATION → Creates NEW Tuple (Because Immutable)
# ---------------------------------------------------------------------
myTuple02 = (10,11,12,13,14,15,16,17,18,19)
print(myTuple01 + myTuple02)


# ---------------------------------------------------------------------
# 🛑 MODIFYING A TUPLE (Not allowed)
# ---------------------------------------------------------------------
# myTuple01[3] = 30  ❌ TypeError (tuple cannot be modified)

# ✔ Correct way → Create NEW tuple by concatenation
myTuple01 = myTuple01[0:2] + (20,21,22,23,24,25,26,27,28,29)
print(myTuple01)


# ---------------------------------------------------------------------
# 🟢 COPY TUPLE → Full slice → new reference but same values
# ---------------------------------------------------------------------
myTuple03 = myTuple01[:]
print(myTuple03)

# 📌 myTuple03 = myTuple01[:] does NOT create a new tuple object.
# Since tuples are immutable, both variables point to the SAME memory location.


# ---------------------------------------------------------------------
# 🧮 Useful Inbuilt Methods
# ---------------------------------------------------------------------
print(len(myTuple03))     # length
print(myTuple03.count(2)) # count occurrences


# ---------------------------------------------------------------------
# 🔍 index() → Find index of element
# ---------------------------------------------------------------------
myTuple04 = (1,2,3,4,5,6,7,8,8,10)
print(myTuple04.index(2)) # index position


# ---------------------------------------------------------------------
# 📌 TUPLE UNPACKING (Destructuring)
# ---------------------------------------------------------------------
(a,b,c,d,e,f,g,h,i,j) = myTuple04
print(a, b, c, d)  # 1 2 3 4

# 📌 Tuple Unpacking assigns each tuple element to separate variables.
# Number of variables must match tuple length.
# Supports * to collect remaining elements in a list.

tup1 = ("Alice", 25, "Delhi")
name, age, city = tup1
print(name, age, city)  # Alice 25 Delhi



# ---------------------------------------------------------------------
# 🛠 Tuple Comprehension → Actually creates a Generator first
# ---------------------------------------------------------------------
myTuple05 = tuple(i for i in range(1, 11))
print(myTuple05)

myTuple06 = tuple(i for i in range(1, 11) if i % 2 == 0)
print(myTuple06)  # (2, 4, 6, 8, 10)


# ---------------------------------------------------------------------
# 🔁 For loop with tuples
# ---------------------------------------------------------------------
for item in myTuple04:
    print(item, end=" ")

# ✔ Tuples are immutable → cannot modify directly → new tuple created
# ✔ Tuples are faster and more memory efficient than lists
# ✔ Good choice for FIXED data or when data should not change
# ✔ Supports all read operations: indexing, slicing, looping
# ✔ Can contain duplicates and any datatype
# ✔ Hashable if all elements are immutable → can be used as dictionary keys
