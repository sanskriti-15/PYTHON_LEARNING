# -----------------------------------------------
# 🔥 PYTHON INTERNAL WORKING (CPython Implementation)
# -----------------------------------------------

# NOTE:
# When you install Python on your local machine,
# you do NOT just install the Python language.
# You install:
#   ✓ Python Interpreter
#   ✓ Python Virtual Machine (PVM)
#   ✓ Standard Library
#   ✓ Built-in Modules
#   ✓ Package Manager (pip)
#   ✓ IDLE (optional)

# So let's understand how Python runs your code internally.
# -----------------------------------------------


# 0️⃣ PYTHON INTERPRETER
# -----------------------------------------------
# ✔ The Python Interpreter is the program responsible for
#   reading your .py script and executing it.
# ✔ When you run:   python index.py
#   → The interpreter takes the script as input.
# ✔ The interpreter performs:
#       1) Lexing (breaking code into tokens)
#       2) Parsing (building syntax tree)
#       3) Compilation into bytecode (.pyc)
#       4) Execution in Python Virtual Machine (PVM)


# 1️⃣ index.py  -> BYTECODE -> PYTHON VIRTUAL MACHINE (PVM)
# ---------------------------------------------------------
# When Python executes your code:
#   index.py  (your Python script)
#       |
#       ↓
#   Compiles into Bytecode  (hidden low-level instructions)
#       |
#       ↓
#   Executed by Python VM (PVM)

# 🔥 This "compile" step is internal and automatic.
# You never see it unless you open the __pycache__ folder.


# 1.a️⃣ COMPILATION STEP — PY → BYTECODE
# -------------------------------------------------------------
# ✔ Python *first compiles* your script into BYTECODE.
# ✔ Bytecode is NOT machine code.
# ✔ It is a low-level, platform-independent instruction set.
# ✔ Bytecode runs FASTER than raw script because:
#       – Parsing & syntax analysis is done only once
#       – Repeated runs can use stored bytecode

# Example of bytecode file:
#       abc.cpython-314.pyc
# Meaning:
#   abc     → your script name
#   cpython → interpreter version
#   314     → Python 3.14
#   .pyc    → Python compiled bytecode


# 1.b️⃣ WHY BYTECODE IS USEFUL?
# ---------------------------------------------------------------
# ✔ Bytecode is independent of OS/CPU.
#   Any machine with Python installed can run it.
# ✔ This is why Python is powerful for:
#       – Cloud services
#       – Distributed systems
#       – Cross-platform apps
# ✔ Bytecode runs on the Python Virtual Machine (PVM).


# 1.c️⃣ WHAT IS A PYTHON .pyc FILE?
# ---------------------------------------------------------------
# ✔ Stored bytecode = .pyc file
# ✔ Python uses these to speed up execution
# ✔ They are NOT source code
# ✔ They are NOT machine code
# ✔ They are intermediate compiled binaries

# Technical name:
#      FROZEN BINARIES


# 1.d️⃣ WHAT ARE "FROZEN BINARIES"?
# ---------------------------------------------------------------
# ✔ Frozen Binaries = Python bytecode that is stored and used
#   during execution.
# ✔ They are executed inside the Python Virtual Machine.

# Python VM = runtime engine that executes bytecode.


# 2️⃣ __pycache__ FOLDER
# ---------------------------------------------------------------
# ✔ This folder contains the .pyc (bytecode) files.
# ✔ When you run your program:
#       Python → Compiles the code → Stores bytecode in __pycache__
# ✔ Deleting __pycache__ does not break your program.
#   It will be recreated automatically.


# ---------------------------------------------------------------
# 🌟 EXTRA IMPORTANT NOTES (ADDED FOR CLARITY)
# ---------------------------------------------------------------

# 🔹 Python has 3 major steps of execution:
#       Source Code (.py)
#               ↓
#       Bytecode (.pyc)
#               ↓
#       Python Virtual Machine (PVM)

# 🔹 PVM is part of the interpreter and is responsible for:
#       – Memory management
#       – Garbage collection
#       – Thread scheduling
#       – Running bytecode instructions

# 🔹 CPython is the official and most widely used implementation of Python.
#   (Other versions: Jython, PyPy, IronPython)

# 🔹 Python is both:
#       – Interpreted (because PVM executes instruction-by-instruction)
#       – Compiled (because it compiles to bytecode first)

# ---------------------------------------------------------------
# END OF PYTHON NOTES ✨
# ---------------------------------------------------------------
