# ============================================================
# IMMUTABLE vs MUTABLE DATA TYPES IN PYTHON
# ============================================================

# 1️⃣ DATA TYPES CLASSIFICATION
# ------------------------------------------------------------

# Immutable Data Types (cannot be changed in-place)
# ------------------------------------------------
# • int
# • float
# • bool
# • str (string)
# • tuple
# • frozenset
# • bytes

# Mutable Data Types (can be changed in-place)
# ------------------------------------------------
# • list
# • set
# • dict (dictionary)
# • bytearray
# • array (from array module)


# 2️⃣ CONCEPT BEHIND IMMUTABLE & MUTABLE DATA TYPES
# -------------------------------------------------------------

# ✔ In Python, EVERYTHING is stored in memory as an OBJECT.
# ✔ Variables only store a REFERENCE (pointer) to that object.

# ❗ Difference is in memory modification behavior:

# IMMUTABLE:
# - Cannot modify existing object
# - New value = new object created in memory
# - Old object removed by Garbage Collector if unused

# MUTABLE:
# - Object can be updated/modified inside same memory location
# - No new memory allocation required


# ============================================================
# 3️⃣ IMMUTABLE EXAMPLE — INTEGER MEMORY BEHAVIOR
# ============================================================

a = 10
b = a  # b points to same object as a
print(id(a), id(b))  # Output: same memory address

a = 20  # new value assigned
print(id(a), id(b))  # a → NEW memory, b → OLD memory

# ✔ int is immutable → value change = new memory allocated


# ============================================================
# 4️⃣ IMMUTABLE EXAMPLE — STRING BEHAVIOR
# ============================================================

x = "chai"
print(id(x))
x = x + " lover"  # string modification creates NEW object
print(id(x))

# ✔ Strings CANNOT be changed in place
# ✔ x now points to a new memory location


# ============================================================
# 5️⃣ MUTABLE EXAMPLE — LIST BEHAVIOR
# ============================================================

lst = [1, 2, 3]
print(id(lst))
lst.append(4)  # modifies the same object in-memory
print(id(lst))

# ✔ Memory address stays SAME
# ✔ List is MUTABLE (update happens inside existing memory)


# ============================================================
# 6️⃣ DICTIONARY MUTABILITY EXAMPLE
# ============================================================

user = {"name": "Ram", "age": 20}
print(id(user))
user["age"] = 21  # in-place modification
print(id(user))

# ✔ dict is mutable → only content updated


# ============================================================
# 7️⃣ KEY TAKEAWAYS FOR INTERVIEWS
# ============================================================

# • Mutable objects allow in-place modifications.
# • Immutable objects create a NEW object when updated.
# • Garbage Collector removes old unused objects automatically.
# • Tuples are immutable but can contain mutable items inside:
my_tuple = (1, [2, 3], 4)
my_tuple[1].append(99)  # Allowed → list inside tuple is mutable

# • Strings are IMMUTABLE → methods like replace(), upper()
#   always return a NEW string.


# 💡 Real-Life Meaning:
# Immutable = constant things (IDs, names stored safely)
# Mutable = dynamic & changeable objects (carts, user settings)

# ============================================================
# END OF NOTES ✔🔥
# ============================================================
