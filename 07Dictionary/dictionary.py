# =====================================================================
# 📘 DICTIONARY (dict) — MUTABLE & UNORDERED KEY-VALUE DATA STRUCTURE
# =====================================================================
# ✔ Stores data in key:value pairs
# ✔ Keys must be UNIQUE & IMMUTABLE (str, int, tuple, etc.)
# ✔ If duplicate keys are used → the last one wins.
# ✔ Python will silently replace older key-value without any error or warning.
# ✔ Values can be ANY datatype (even lists or dicts!)
# ✔ Mutable: can update, add, remove items
# =====================================================================

myDict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(myDict)  # {'name': 'John', 'age': 30, 'city': 'New York'}


# ---------------------------------------------------------------------
# 📌 Dictionary Indexing / Access Values
# ---------------------------------------------------------------------
print(myDict["name"])  # John
print(myDict["age"])   # 30
print(myDict["city"])  # New York

# NOTE: If key does not exist → KeyError ❌


# ---------------------------------------------------------------------
# 📌 Update Existing Value
# ---------------------------------------------------------------------
myDict["city"] = "Los Angeles"
print(myDict)  # city updated ✔


# ---------------------------------------------------------------------
# 📌 Dictionary Concatenation
# (Dictionaries do NOT support + operator ❌)
# ---------------------------------------------------------------------

dict1 = {"A": 1, "B": 2, "C": 3}
dict2 = {"D": 4, "E": 5, "F": 6}

# Method-1 → | operator (Python 3.9+)
dict3 = dict1 | dict2
print(dict3)


# Method-2 → ** Unpacking
myDict2 = {"name": "Robert", "age": 25, "city": "Miami"}
myDict3 = {"phone": "555", "email": "test@example.com", "address": "123 Street"}

myDict4 = {**myDict2, **myDict3}
print(myDict4)


# Method-3 → update() method
dict3 = {"a": 1, "b": 22}
dict4 = {"b": 333, "c": 4444}

dict3.update(dict4)
print(dict3)
# ✔ If key already exists → NEW value replaces OLD value


# ---------------------------------------------------------------------
# 📌 Check if key exists
# ---------------------------------------------------------------------
if "name" in myDict:
    print("name exists")


# ---------------------------------------------------------------------
# 📌 Dictionary Comprehension
# ---------------------------------------------------------------------
myDict5 = {x: x ** 2 for x in range(1, 6)}
print(myDict5)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ---------------------------------------------------------------------
# 📌 Looping through Dictionary
# ---------------------------------------------------------------------
for key in myDict:
    print(key)  # prints keys

for key in myDict:
    print(key, myDict[key])  # prints both

for value in myDict.values():
    print(value)  # prints values

for key, value in myDict.items():
    print(key, value)  # prints both

# ---------------------------------------------------------------------
# 📌 Access Using get() — Safer than indexing ✔
# ---------------------------------------------------------------------
print(myDict.get("name"))     # John
print(myDict.get("address"))  # None instead of KeyError


# ---------------------------------------------------------------------
# 📌 len() → Count total key:value pairs
# ---------------------------------------------------------------------
count_dict = {"one": 1, "two": 2, "three": 3}
print(len(count_dict))  # 3


# ---------------------------------------------------------------------
# 📌 Add new key-value
# ---------------------------------------------------------------------
count_dict["four"] = 4
print(count_dict)


# ---------------------------------------------------------------------
# 📌 update() → Add/Modify multiple pairs
# ---------------------------------------------------------------------
count_dict.update({"five": 5})
print(count_dict)


# ---------------------------------------------------------------------
# 📌 copy() → Shallow Copy
# ---------------------------------------------------------------------
count_dict_copy = count_dict.copy()
print(count_dict_copy)

# 📌 dict.copy() creates a shallow copy → new dictionary object with different memory location.
# Changing the original dictionary does not affect the copied one (unless it has nested dictionaries).


# ---------------------------------------------------------------------
# 📌 pop() → Remove specific key
# ---------------------------------------------------------------------
count_dict.pop("four")
print(count_dict)
# ✔ Unlike list.pop(): dict.pop() removes by KEY, not index


# ---------------------------------------------------------------------
# 📌 popitem() → Removes LAST inserted pair
# ---------------------------------------------------------------------
count_dict.popitem()
print(count_dict)


# ---------------------------------------------------------------------
# 📌 del → Delete by Key
# ---------------------------------------------------------------------
del count_dict["three"]
print(count_dict)


# ---------------------------------------------------------------------
# 📌 clear() → Remove all key-value pairs
# ---------------------------------------------------------------------
count_dict.clear()
print(count_dict)  # {}


# ---------------------------------------------------------------------
# 🔥 Nested Dictionary (Dictionary inside dictionary)
# ---------------------------------------------------------------------
desktop_computer = {
    "CPU": {"brand": "AMD", "model": "5600", "clock": "3.5 GHz"},
    "RAM": {"brand": "XPG", "size": "16 GB"},
}
print(desktop_computer["CPU"])
print(desktop_computer["CPU"]["brand"])
print(desktop_computer["RAM"]["size"])


# ---------------------------------------------------------------------
# 📌 zip() → Create Dictionary by combining keys & values
# ---------------------------------------------------------------------
keys = ["CPU_Fan", "Cooler"]
values = [
    {"brand": "Cooler Master"},
    {"brand": "Deepcool"}
]

computer_peripheral = dict(zip(keys, values))
print(computer_peripheral)


# ---------------------------------------------------------------------
# 📌 Merge dictionaries using | operator
# ---------------------------------------------------------------------
total_computer = desktop_computer | computer_peripheral
print(total_computer)


# ---------------------------------------------------------------------
# 📌 fromkeys() → Create dictionary with common default values
# ---------------------------------------------------------------------
keys = ["key1", "key2", "key3"]
default_value = "common_val"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
# ⚠ WARNING:
# dict.fromkeys(keys, value) assigns the SAME value object to all keys.
# If the value is mutable (like list/dict), modifying one key's value will 
# change all → because they share the same reference!


new_dict = dict.fromkeys(keys, keys)
print(new_dict)
# {'key1': ['key1', 'key2', 'key3'],
#  'key2': ['key1', 'key2', 'key3'], 
#  'key3': ['key1', 'key2', 'key3']}

# =====================================================================
# 🎯 FINAL INTERVIEW NOTES
# =====================================================================
# ✔ Ordered (Python 3.7+)
# ✔ Keys must be immutable & unique
# ✔ Values can be any datatype
# ✔ Mutable → can update
# ✔ .get() is safer than []
# ✔ .update() overrides existing keys
# ✔ dict.copy() → shallow copy
# ✔ Supports dictionary comprehension
# ✔ Best for fast lookups (Hash table based)
# =====================================================================
