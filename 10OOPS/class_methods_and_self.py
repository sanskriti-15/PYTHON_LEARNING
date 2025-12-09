# =====================================================================
# 🏎️ CLASS METHOD + SELF → BEST EXPLANATION
# =====================================================================
# ✔ self → represents the current object calling the method
# ✔ Helps in accessing object attributes and object methods
# ✔ Every instance method MUST have `self` as first parameter
# =====================================================================


class Car:

    # __init__() → Constructor → Runs automatically when object is created
    def __init__(self, brand, model):
        self.brand = brand      # Instance variable
        self.model = model      # Instance variable

    # Instance Method → Works on data of specific object using `self`
    def display_full_name(self):
        return f"The full name of the car is: {self.brand} {self.model}"


# Creating an object → memory allocated → constructor runs
my_car = Car("Toyota", "Camry")

# Method call → my_car is automatically passed as `self`
print(my_car.display_full_name())
