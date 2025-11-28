# ===============================================================
# PYTHON REPL + IMPORTS + ERRORS + LOOPS + SYS/OS MODULE NOTES
# ===============================================================


# ◼ STARTING PYTHON IN VS CODE TERMINAL
# ---------------------------------------
# Command used:
# >>> python
#
# Opens Python in open in integrated folder → Lets us test Python line-by-line


# ◼ BASIC STRING & NUMBER OPERATIONS
# ---------------------------------------
"sanki" * 4
# Output:
# 'sankisankisankisanki'

score = 100
print(score)
# Output: 100


# ◼ STRING vs VARIABLE
# ---------------------------------------
print("sanki")    # OK → string printed
# Output: sanki

# sanki      
# ❌ Not defined as variable
# NameError: name 'sanki' is not defined


# ◼ WORKING WITH OS MODULE
# ---------------------------------------
import os
os.getcwd()
# Output shows current working directory of VS Code terminal


# ◼ COMMON ERRORS IN PYTHON REPL
# ---------------------------------------

# ❌ ERROR: invalid variable name
#  >>> for loop = start
# SyntaxError: invalid syntax

# ✔ Correct:
for_loop = "start"
print(for_loop)
# Output: start


# ❌ ERROR: Missing quotes around a string
#     >>> for_loop = start
# NameError: name 'start' is not defined


# ❌ ERROR: Colon missing in loop
#   >>> for elements in "start"
# SyntaxError: expected ':'


# ✔ Correct loop (from screenshot)
for elements in "start":
    print(elements)

# Output:
# s
# t
# a
# r
# t


# ◼ SYS MODULE USAGE
# ---------------------------------------
import sys
sys.version   # Shows Python version
sys.platform  # Shows OS
# Output: 'linux'


# ◼ IMPORTING basics.py MODULE
# ---------------------------------------
import basics
# Output printed:
# 9
# 170
# 4

# After importing a module, you can access its functions
# using dot notation:
basics.fun("abcd")
# Output:
# abcd


# ❌ WRONG WAY: Calling a function inside import statement
# >>> import basics.fun("masala chai")
# SyntaxError: invalid syntax
#
# Reason:
# "import" can only import modules/packages, not call functions.


# -----------------------------------------------------------
# IMPORTANT CONCEPT ABOUT MODULE DATA IN MEMORY
# -----------------------------------------------------------

# When you import a module (in REPL or Python Shell):
# >>> import basics

# Python loads the MODULE INTO MEMORY (not from file every time)


# If you LATER add new functions or variables inside basics.py
# Those NEW changes WILL NOT appear automatically inside REPL.


# Example Problem:
# >>> basics.var1
# AttributeError: module 'basics' has no attribute 'var1'
#
# Why?
# When first imported → var1 did NOT exist inside basics.py


# ❌ AttributeError (Before Updating Module)
# >>> basics.fun01
# AttributeError: module 'basics' has no attribute 'fun01'


# -----------------------------------------------------------
# Solution → RELOAD THE MODULE
# -----------------------------------------------------------
from importlib import reload
reload(basics)
# Output:
# Module reloaded successfully

# ✔ Now new functions and variables inside basics.py
#   become available in REPL.

# ===========================================================
# Will module changes update automatically in VS Code Run Mode?
# ===========================================================
# ✘ No reload() needed here.

# When you click RUN / F5 in VS Code:

#   ✔ Python interpreter restarts fresh every time
#   ✔ No old module remains in memory
#   ✔ All latest changes in basics.py load automatically

# So, reload(basics) is ONLY required in:
#     ▸ REPL (>>>)
#     ▸ Interactive Shell
#     ▸ Jupyter Notebook

# NOT needed in:
#     ▸ Run button in VS Code
#     ▸ Running .py script normally

# In simple words:
#     REPL keeps memory → needs reload()
#     VS Code Run restarts fresh → no reload needed
# ===========================================================


# 🧠 KEY TAKEAWAY:
# Python does NOT auto-refresh imported modules.
# reload() is required after updating a module while REPL is running.
# ===========================================================


# ✔ Now variables or attributes exist (after updating basics.py)
basics.chai02
# Output: normal chai

basics.chai03
# Output: hot chai

basics.chai04
# Output: iced chai


# ◼ IMPORTANT RULES LEARNED
# ---------------------------------------
# ✔ Python REPL executes code line by line
# ✔ Every function must be imported before calling
# ✔ Always reload() after editing modules
# ✔ Strings need quotes
# ✔ Loops must end with :
# ✔ Variables cannot have spaces
# ✔ import index → runs code in index.py automatically


# ◼ VS CODE INTEGRATED TERMINAL (VERY IMPORTANT)
# -----------------------------------------------
# • Used to run Python directly from VS Code
# • Open using: Ctrl + `
# • Commands:
#       python file.py  → Run script
#       python          → Enter REPL
#       exit() or Ctrl + Z → Exit REPL
# • Shows current working directory (CWD)
# • Allows testing imports, loops, code quickly

