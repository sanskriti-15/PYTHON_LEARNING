# =====================================================================
# 🔍 SCOPE / NAMESPACE IN PYTHON
# =====================================================================
# Scope = Region where a variable is recognized and can be accessed.
# Python mainly uses two scopes in functions:
#
# 1️⃣ GLOBAL SCOPE
#    - Variables defined outside any function
#    - Accessible everywhere in the file/program
#
# 2️⃣ LOCAL SCOPE
#    - Variables defined inside a function
#    - Accessible only inside that function
#
# ✔ Python always tries to resolve a variable using:
#      LEGB Rule = Local → Enclosed → Global → Built-in
# =====================================================================


# =====================================================================
# 🟣 GLOBAL SCOPE EXAMPLE
# =====================================================================
new_list = [1,2,3]  # Global variable

def my_function_01():
    for i in new_list:  # Accessing global scope inside function
        print(i)

my_function_01()
print("\n")


# =====================================================================
# 🔁 GLOBAL Keyword → Convert Local variable to Global
# =====================================================================
any_variable = 82  # Global variable

def function_with_global_method():
    global any_variable  # Now this refers to global scope
    any_variable = 33  # Modifies global variable
    print("Inside function:", any_variable)

function_with_global_method()
print("Outside function:", any_variable)
print("\n")

# ✔ NOTE:
# global keyword allows function to modify the global variable
# otherwise Python creates a new local variable of same name.


# =====================================================================
# 🟡 LOCAL SCOPE EXAMPLE
# =====================================================================
def my_function_02():
    num_01 = 5   # Local
    num_02 = 13  # Local
    return num_01 + num_02

print(my_function_02())
print("\n")

# print(num_01) ❌ Error → num_01 not accessible outside function


# =====================================================================
# 🌐 LOCAL SCOPE EXISTING IN CHILD FUNCTIONS
# =====================================================================
def my_function_02_DEMO():
    num_01 = 88
    def child_function():
        print(num_01)  # Allowed → child can access parent's local variable
    child_function()

my_function_02_DEMO()
print("\n")


# =====================================================================
# 🎯 USING LOCAL VARIABLES AS FUNCTION PARAMETERS
# =====================================================================
def my_function_02():
    num_01 = 5
    num_02 = 13
    def sum_func(value01, value02):
        return value01 + value02
    return sum_func(num_01, num_02)

print(my_function_02())
print("\n")


# =====================================================================
# 🧮 LOCAL SCOPE SHARING BETWEEN MULTIPLE CHILD FUNCTIONS
# =====================================================================
def my_function_03():
    num_01 = 5
    num_02 = 13

    def sum_func(x, y):
        return x + y

    def mul_func(x, y):
        return x * y

    return ( sum_func(num_01, num_02),
             mul_func(num_01, num_02) )

print(my_function_03())
print("\n")


# =====================================================================
# 🔥 CLOSURES IN PYTHON → ALSO CALLED "BAGGAGE FUNCTIONS"
# =====================================================================
# ✔ Closure = A function inside another function (child)
# ✔ Parent returns the child function
# ✔ Returned child remembers variables from parent function
#
# Meaning:
# - Even after parent function finishes execution
# - Child function STILL retains access to parent's local variables
# =====================================================================

def func_01():
    x_val = 17
    def child_func_01():  # child function uses parent's local variable
        print(x_val)
    return child_func_01  # returning function definition (closure)

result01 = func_01()
result01()  # Prints 17 → Parent is gone, but data remains!


x_value = 55

def my_function_04():
    # x_value = 99 (Local) ❌ commented out
    print("From Parent:", x_value)  # Global 55

    def lookup_func_01():
        print("From Child 1:", x_value)

    def lookup_func_02():
        print("From Child 2:", x_value)

    lookup_func_01()
    lookup_func_02()

my_function_04()
print("\n")


# =====================================================================
# 🧲 CLOSURE EXAMPLE — FUNCTION RETURNING ANOTHER FUNCTION
# =====================================================================

def chaicode(num_P):       # Parent function
    def actual(num_C):     # Child function using parent's variable
        return num_C ** num_P
    return actual          # Closure → returns child + parent's remembered value

# chaicode(2) returns a function that squares numbers
square_result = chaicode(2)

# chaicode(3) returns a function that cubes numbers
cube_result = chaicode(3)

print(square_result(4))   # 4^2 = 16
print(cube_result(3))     # 3^3 = 27


# L → Local (inside current function)
# E → Enclosing (outer function variables for nested functions)
# G → Global (outside of all functions)
# B → Built-in (Python’s predefined functions like print, len, sum...)


# ✔ Global variables can be read inside functions
# ✔ To modify global inside function → use global keyword
# ✔ Child functions can access parent's local scope (closure)
# ✔ Closure keeps data alive even after parent’s execution ends
# ✔ Python follows LEGB precedence to resolve variables
