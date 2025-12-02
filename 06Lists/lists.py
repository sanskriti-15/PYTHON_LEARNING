# =====================================================================
# 📌 LISTS IN PYTHON — MUTABLE SEQUENCE DATA TYPE
# =====================================================================
# ✔ Can store different datatypes together
# ✔ Indexed (supports positive and negative indexing)
# ✔ Mutable → values can be changed in-place
# ✔ Ordered → preserves insertion order
# ✔ Allows duplicates
# Strings are immutable → modify string → new memory created
# Lists are mutable → modify list → same memory updated
# =====================================================================


# ---------------------------------------------------------------------
# BASIC LIST CREATION & INDEXING
# ---------------------------------------------------------------------
numList = [1, 2, 3, 4]
print(numList)

numList2 = numList
print(numList2 is numList)  #true
# 📌 numList2 = numList → No copy is created.
#    Both variables refer to the SAME list in memory.
#    So changing numList will also change numList2 (and vice-versa).
#    This is because LISTS are MUTABLE, unlike STRINGS where a new memory
#    is created on modification.

print(numList[0])  # 1
print(numList[1])  # 2
print(numList[2])  # 3

# Negative indexing (access from end)
print(numList[-1])  # 4
print(numList[-2])  # 3
print(numList[-3])  # 2


# ---------------------------------------------------------------------
# LIST SLICING → [start:end:step]
# ---------------------------------------------------------------------
print(numList[0:2])  # [1, 2]
print(numList[:2])   # [1, 2]
print(numList[2:])   # [3, 4]
print(numList[:])    # Full copy (SHALLOW COPY) → new list but same inner references

#✔ Case 1 — A has only simple values (ints, strings)
A = [1, 2, 3]
B = A[:]    # New separate list
A[0] = 99
print(B)  # No change

#❗Case 2 — A has nested list(s)
A = [1, 2, [3, 4]]
B = A[:]
A[2][0] = 999
print(B)  # B changes also!

# 📌 A[:] creates a new list (different memory), but if the list contains nested lists,
#    the nested items still share the same memory → changing inner elements affects both lists.


# ---------------------------------------------------------------------
# LIST CONCATENATION
# ---------------------------------------------------------------------
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)  # [1,2,3,4,5,6]


# ---------------------------------------------------------------------
# STRING FORMAT WITH LIST VALUES
# ---------------------------------------------------------------------
list4 = ["Python", "is", "fun"]
statement = "Today we will try {} for the {} time"
print(statement.format(list4[0], list4[2]))


# ---------------------------------------------------------------------
# REPLACING ELEMENTS (MUTABLE BEHAVIOR)
# ---------------------------------------------------------------------
list4[2] = "learning"
print(list4)  # ['Python', 'is', 'learning']

# Slice replacing → expands characters if replacing with string directly
list4[0:1] = "Java"
print(list4)  # ['J','a','v','a','is','learning'] → ❌ BAD
print(len(list4))

# Fix slice replacement by wrapping value in list
list4 = ["Python", "is", "fun"]
list4[0:1] = ["Java"]  # ✔ correct
print(list4)

list4[0:2] = ["JavaScript", "will be"]
print(list4)


# ---------------------------------------------------------------------
# INSERTING WITH SHIFTING (NO REPLACE)
# ---------------------------------------------------------------------
shift_list = ['A','B','C','D','E','F','G','H']

# Insert at index 1 and shift right
shift_list[1:1] = ['X','Y','Z']
print(shift_list)  # ['A', 'X', 'Y', 'Z', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


# Remove by slicing
shift_list[1:4] = []
print(shift_list) # from 1 to 4 (excluding) add empty array ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# [:] copy list (shallow)
shift_list_copy = shift_list[:]
print("shift_list_copy:", shift_list_copy)

shift_list_copy[0:] = []  # Clear using slicing
print(shift_list_copy)


# ---------------------------------------------------------------------
# COPYING LISTS
# ---------------------------------------------------------------------
list5 = list2.copy()  # New list (separate reference)
list2[1] = 99
print(list2)  # Change in original ✔
print(list5)  # list5 unaffected ✔


# ---------------------------------------------------------------------
# INSERT, APPEND, LENGTH
# ---------------------------------------------------------------------
list5 += [7,8,9,10,11,12,13]  # Extend list
list5.insert(0, 99)  # Add at index
print(list5) # [99, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(len(list5))  # Length of list

list5.append(5)  # Add at end
print(list5)


# ---------------------------------------------------------------------
# COUNTING ELEMENT
# ---------------------------------------------------------------------
print(list5.count(5))  # Count appearances of 5


# ---------------------------------------------------------------------
# SORTING & REVERSING
# ---------------------------------------------------------------------
list5.sort()     # Ascending
print(list5)

list5.reverse()  # Reverse order
print(list5)


# ---------------------------------------------------------------------
# REMOVING ELEMENTS
# ---------------------------------------------------------------------
list5.pop()  # Removes last element
print(list5)

list6 = list(range(10))
list6.remove(8)  # Remove value (not index)
print(list6)


# ---------------------------------------------------------------------
# FIND INDEX OF ELEMENT
# ---------------------------------------------------------------------
print(list6.index(3))  # index of value 3


# ---------------------------------------------------------------------
# DELETE USING DEL
# ---------------------------------------------------------------------
list7 = ['a','b','c','d','e','f','g','h']
print(list7)

del list7[4]  # Delete item by index
print(list7)


# ---------------------------------------------------------------------
# MEMBERSHIP TEST
# ---------------------------------------------------------------------
if "e" in list7:
    print("e is present in list7")
else:
    print("e not present")


# ---------------------------------------------------------------------
# CLEARING LIST
# ---------------------------------------------------------------------
list6.clear()  # Removes all elements
print(list6)


# ---------------------------------------------------------------------
# RANGE → LIST
# ---------------------------------------------------------------------
range_value = range(10)
print(range_value) # range(0, 10)

print(list(range_value))  # Convert into list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ---------------------------------------------------------------------
# ITERATING THROUGH LIST
# ---------------------------------------------------------------------
for elements in list5:
    print(elements, end="-")  # Print in one line with separator


# ---------------------------------------------------------------------
# LIST COMPREHENSION → Very IMP for interviews
# ---------------------------------------------------------------------
list8 = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in list8]
print(squares)

cube = [x**3 for x in range(1,11)]
print(cube)


# ---------------------------------------------------------------------
# 🎯 FINAL IMPORTANT NOTES FOR LISTS
# ---------------------------------------------------------------------
# ✔ Mutable → original list changes without new memory
# ✔ Supports dynamic resizing
# ✔ Supports slicing, indexing, negative index
# ✔ list.copy(), slicing [:] → shallow copy
# ✔ append(), insert(), remove(), pop(), sort(), reverse(), clear()
# ✔ list comprehension → most used in real projects
# ✔ Lists allow mixed datatypes and duplicates
# =====================================================================
