# =====================================================================
# 📌 DECORATORS IN PYTHON
# =====================================================================
# ✔ Decorator = A function that modifies another function’s behavior
# ✔ Decorators add extra features → **without changing original function code**
# ✔ Used for:
#      ◼ Logging
#      ◼ Authentication
#      ◼ Timing Function Execution
#      ◼ Debugging / Validation
# ✔ Behind the scenes, decorators **wrap** a function inside another function
# =====================================================================


# ---------------------------------------------------------------------
# 🎯 FUNCTION DECORATOR EXAMPLE — BEST EXPLANATION
# ---------------------------------------------------------------------

# This is a decorator function
def decorator_function(original_function):

    # Wrapper function adds extra behavior around original function
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed BEFORE {original_function.__name__}")  
        # Calling the original function inside wrapper
        return original_function(*args, **kwargs)

    return wrapper_function   # Returning wrapper modifies original function



# ---------------------------------------------------------------------
# @decorator_function applies the decorator to display()
# Equivalent to:
#        display = decorator_function(display)
# ---------------------------------------------------------------------
@decorator_function
def display():
    print("display function ran")



# Calling the function normally, but wrapper runs first → decoration applied
display()


# =====================================================================
# FINAL NOTES (WRITE IN NOTEBOOK)
# =====================================================================
# ✔ Decorator adds functionality around an existing function
# ✔ @decorator_name is just a shortcut for:
#       function = decorator_name(function)
# ✔ Wrapper executes before/after original function
# ✔ Decorators support arguments using (*args, **kwargs)
# ✔ Great for clean, reusable code without touching original function
# =====================================================================
