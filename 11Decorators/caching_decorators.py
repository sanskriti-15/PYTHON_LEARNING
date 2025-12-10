# =====================================================================
# 🗂️ QS.03 — CACHE RETURN VALUES USING DECORATOR
# =====================================================================
# ✔ Problem: Avoid re-running expensive functions (slow APIs, DB calls, heavy computation)
# ✔ Solution: Use a decorator to STORE previous results in a CACHE
# ✔ When same arguments repeat → return stored result instead of recomputing
# ✔ This improves speed & performance
# =====================================================================


import time   # Used to simulate slow processing

# ---------------------------------------------------------------
# Caching decorator
# ---------------------------------------------------------------
def cache(function):

    # Local dictionary to store results → key=arguments, value=result
    cache_value_dict = {}
    print("Initial cache:", cache_value_dict)

    def wrapper(*args, **kwargs):

        # If same arguments exist → return old result instantly
        if args in cache_value_dict:
            print("Fetching cached result for:", args)
            return cache_value_dict[args]

        # Otherwise call original function
        result = function(*args, **kwargs)
        print("Storing result in cache for:", args)

        # Save result in cache
        cache_value_dict[args] = result

        return result
    
    return wrapper  # Return wrapper definition so decorator works



# ---------------------------------------------------------------
# Slow function → takes time (simulating heavy task)
# ---------------------------------------------------------------
@cache   # Adding cache functionality
def long_running_function(num01, num02):
    time.sleep(4)     # Delay to simulate slowness
    return num01 + num02



# ---------------------------------------------------------------
# Execution
# ---------------------------------------------------------------
result_01 = long_running_function(1, 2)  # Takes ~4 seconds (no cache)
result_02 = long_running_function(1, 2)  # Instant result (from cache)

print("From result_01:", result_01)
print("From result_02:", result_02)


# =====================================================================
# FINAL IMPORTANT NOTES
# =====================================================================
# ✔ Dictionary used for caching makes repeated calls faster
# ✔ Saves time by not recalculating same inputs again
# ✔ Works best for functions with:
#       ◼ same input → same output (pure functions)
# ✔ Key stored as args tuple → must be hashable
# ✔ Common name: Memoization → technique used in optimization & DP
# =====================================================================
