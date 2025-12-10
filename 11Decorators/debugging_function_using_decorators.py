# =====================================================================
# 🐞 QS.02 — DEBUGGING FUNCTION CALLS USING DECORATORS
# =====================================================================
# ✔ This decorator prints:
#       → Function name being called
#       → Arguments passed to the function
#       → Return value produced
# ✔ Helps track and debug function behavior
# =====================================================================


# ---------------------------------------------------------------
# Decorator to log function name, arguments and output
# ---------------------------------------------------------------
def debug_function(function):
    def wrapper(*args, **kwargs):

        result = function(*args, **kwargs)  # running original function

        # Debug print statement
        print(f"The function '{function.__name__}' was called with arguments {args} "
              f"and returned value: {result}")

        return result  # return original result
    
    return wrapper  # returning wrapper definition



# ---------------------------------------------------------------
# Applying decorator to custom function
# ---------------------------------------------------------------
@debug_function
def addSum(*args):
    return sum(args)


addSum(1, 2, 3, 4, 5)   # Debug info printed
addSum(55, 11)          # Debug info printed



# =====================================================================
# 🔍 More Enhanced Debug Decorator (Sir’s Code) — Better Formatting
# =====================================================================

def debug(function):
    def wrapper(*args, **kwargs):

        # Formatting args and kwargs to string for clean printing
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{key}={value}" for key, value in kwargs.items())

        result = function(*args, **kwargs)

        print(f"\ncalling: {function.__name__} function "
              f"with args({args_value}) and kwargs({kwargs_value})")

        return result
    
    return wrapper



# Testing enhanced decorator
@debug
def hello():
    print("hello")

hello()  # No arguments, so empty display


@debug
def greet(name, statement='Hello!!'):
    print(f"{statement} I am {name}")

greet('Munna', statement='Hi')


# =====================================================================
# FINAL NOTES
# =====================================================================
# ✔ Decorators can track function calls for debugging
# ✔ wrapper logs name, args, kwargs, and output
# ✔ Very helpful in large applications (analytics, error tracking, logging)
# ✔ We always return wrapper → so original functional behavior is preserved
# =====================================================================
