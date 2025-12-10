# =====================================================================
# ⏱️ QS.01 — TIMING FUNCTION EXECUTION USING DECORATORS
# =====================================================================
# ✔ Decorator used to measure how long a function takes to run
# ✔ Useful for performance testing & optimization
# ✔ Uses time.time() to calculate execution duration
# =====================================================================


import time   # For tracking start & end time of function execution


# ---------------------------------------------------------------
# Decorator function → adds timing feature to any function
# ---------------------------------------------------------------
def timer(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()   # Before function executes

        result = function(*args, **kwargs)  # Calling the function

        end_time = time.time()     # After function executes

        # Printing time difference
        print(f"Function {function.__name__} took {end_time - start_time} seconds to execute")

        return result   # Returning original result (important!)
    
    return wrapper  # Returning wrapper definition to apply decorator



# ---------------------------------------------------------------
# Applying decorator using @timer
# ✔ Adds timing measurement BEFORE running the function
# ---------------------------------------------------------------
@timer
def example_function(time_sleep):
    time.sleep(time_sleep)   # Simulates heavy process by sleeping



# Testing the performance
example_function(2)  # Output: ~2 seconds


# =====================================================================
# FINAL NOTES
# =====================================================================
# ✔ Decorator adds extra functionality WITHOUT modifying original function
# ✔ wrapper collects args/kwargs → supports flexible functions
# ✔ return result ensures original function output is preserved
# ✔ Used in profiling, debugging & optimizing large systems
# =====================================================================
