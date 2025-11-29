# ==================================================================
# PYTHON DATA TYPES / OBJECT TYPES 
# ==================================================================

# Python is a Dynamically Typed Language:
# ➝ You do NOT need to declare type of variable
# ➝ It is decided automatically at runtime
# type()  ➝ tells datatype of a value
# dir()  ➝ shows all available functions/attributes of that datatype


# ================================================================
# 1️⃣ NUMBERS
# ================================================================
# Numeric data used in mathematical operations

a = 1234          # Integer (whole numbers)
b = 3.1468        # Float (decimal numbers)
c = 3 + 4j        # Complex number (real + imaginary part)
d = 0b1010        # Binary literal representation ➝ value: 10

import math
math.pi

import random
random.random()
random.choice([1,2,3,4])

# Decimal — used where HIGH precision is required (finance apps)
from decimal import Decimal
e = Decimal('10.56')
print(e, type(e))

# Fraction — maintains exact fractional values
from fractions import Fraction
f = Fraction(3, 4)
print(f, type(f))

print(b)
print(type(a), type(c), type(f))


# ================================================================
# 2️⃣ STRING (Text Data)
# ================================================================
# Strings store characters/text ➝ Immutable (cannot modify in-place)

s1 = 'Hello'
s2 = "Hello"
s3 = "Bob's world"       # Single quotes inside double quotes allowed

# s1[0] = 'g'  this is an error 
s1[1:3]  
s1[1:]
s1[-1]

dir(s1) # this will give all the functions that will be given to s1

# Special string types
s4 = b'a\x01c'           # Bytes literal ➝ value stored in binary
s5 = u'sp\u00e9cial'     # Unicode string (supports 🔥 emojis & accents)

print(s3, s5)


# ================================================================
# 3️⃣ LIST — MUTABLE SEQUENCE
# ================================================================
# Ordered, allows mixed data types, can change values in-place

lst1 = []                                # Empty List
lst2 = ['Hello', 'World']                # String List
lst3 = [1, 2, "3"]                        # Mixed types allowed
lst4 = ['foo', 'bar', ['baz', 'qux']]    # Nested List
lst5 = list(range(10))                   # List of numbers 0-9

len(list1)
list2[-1]
list2[1:3]
lst2.append("Python")  # Modifies existing list, no new memory created

print(lst4, id(lst4))   # id() shows memory address


# ================================================================
# 4️⃣ TUPLE — IMMUTABLE SEQUENCE
# ================================================================
# Ordered like list BUT cannot modify values (safer for fixed data)

t1 = ()
t2 = (1, 2, 3)
t3 = (1, 2, "3")
t4 = ('foo', 'bar', ('baz', 'qux'))   # Nested tuple
t5 = tuple(range(10))                 # Converted from range to tuple

# Special Tuple type ➝ namedtuple (data stored with keys)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print(t4, p.x)     # Access using attribute name ➝ p.x = 10


# ================================================================
# 5️⃣ BOOLEAN DATA TYPE
# ================================================================
# Logical values ➝ Used in conditions

flag1 = True
flag2 = False
print(type(flag1))


# ================================================================
# 6️⃣ MAPPING — DICTIONARY (KEY:VALUE pairs)
# ================================================================
# Unordered, Mutable, Values accessed using Key

d1 = {}                                   # Empty dictionary
d2 = {'one': 1, 'two': 2, 'three': 3}     # Key:Value
d3 = dict(one=1, two=2, three=3)          # Alternate syntax

print(d2['two'])   # Access value using key

# ❗Important:
# Keys must be immutable → strings, numbers, tuples


# ================================================================
# 7️⃣ SET — UNIQUE & UNORDERED COLLECTION
# ================================================================
# Automatic duplicate removal, great for membership checks

s1 = {1, 2, 3}
s2 = set([1, 2, 3, 59, 1, 8])  # Duplicate 1 removed
s3 = set('Mississippi')        # Unique characters only

print(s2, s3)


# ================================================================
# 8️⃣ FILE TYPE — File Operations (IO)
# ================================================================
# Used for reading/writing files on disk

# f = open('test.txt', 'w')      # Write mode (overwrite file)
# f = open('test.txt', 'r')      # Read mode
# f = open('test.txt', 'a')      # Append mode (add data)
# f = open(r'c:\test.txt', 'wb') # Binary mode
# f.close()                      # Always close file after use!


# ================================================================
# 9️⃣ BUFFER / BINARY DATA TYPES
# ================================================================
# Used for raw byte manipulation (images, network data)

buf1 = bytes([65, 66, 67])     # Immutable bytes
buf2 = bytearray([65, 66, 67]) # Mutable bytes
buf2[1] = 90                   # Changing value in-place ➝ allowed

buf3 = memoryview(buf1)        # Provides direct access to memory

print(buf1, buf2)


# ================================================================
# 🔟 NONE TYPE — no value / empty value representation
# ================================================================
x = None
print(x is None)  # True


# ================================================================
# 1️⃣1️⃣ FUNCTION TYPE
# ================================================================
# Code block stored as an object

def func():
    return "Hello Function!"

lam = lambda x: x * 2  # Anonymous inline function

print(func(), lam(4))


# ================================================================
# 1️⃣2️⃣ MODULE TYPE
# ================================================================
# A module = Python file containing functions, classes etc.

# import math
# import module as m
# from module import func
# from module import *      # Not recommended (namespace confusion)


# ================================================================
# 1️⃣3️⃣ CLASS & OBJECT TYPES
# ================================================================
# Blueprint for creating objects (Object-Oriented Programming)

class Person:
    def __init__(self, name):
        self.name = name

obj = Person("Ram")
print(obj.name)


# ================================================================
# 1️⃣4️⃣ ADVANCED PYTHON OBJECT TYPES
# ================================================================
# • Generator → Produces values on demand (memory efficient)
# • Iterator → Used to iterate elements one-by-one
# • Decorator → Enhances behavior of functions
# • Metaclass → Class that creates classes

gen = (i for i in range(5))   # Simple generator
print(next(gen))              # next() gives next value


# ================================================================
# FINAL IMPORTANT NOTES
# ================================================================
# ✔ Everything in Python is an OBJECT
# ✔ Python is Dynamically Typed
# ✔ Object type can be checked using type()
# ✔ Internal methods explored using dir()
# ✔ Mutable → list, set, dict (changes in same memory)
# ✔ Immutable → int, str, tuple (new memory on change)
# ✔ dict, list, set are MOST IMPORTANT in coding
# ✔ Tuples used for fixed data (safer)
# ✔ Strings support Unicode (global language support)
# ✔ Generators best for huge data (no memory wastage)
# ================================================================
