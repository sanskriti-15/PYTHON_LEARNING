# =====================================================================
# 🚗 CLASS VARIABLES IN PYTHON — BEST EXPLANATION
# =====================================================================
# ✔ Class Variable → Shared by ALL objects of the class
# ✔ Instance Variable → Unique for each object
#
# 👉 Class variables help store data common to all objects
#    Example: Counting number of cars created
# =====================================================================


class Car:
    # 🎯 CLASS VARIABLE — belongs to class
    total_cars = 0

    def __init__(self, brand, model):
        # 🔹 Instance Variables — belong to object
        self.brand = brand
        self.model = model

        # Increase class variable when new object created
        Car.total_cars += 1  # ✔ Correct way


    # Instance methods
    def fuel_type(self):
        return "Petrol"

    def display_full_name(self):
        return f"{self.brand} {self.model}"


# Creating multiple objects → count increases
Car("Toyota", "Camry")
Car("Ford", "Mustang")
Car("Mazda", "3")
Car("Ferrari", "F8")

print(Car.total_cars)  # ✔ 4



# =====================================================================
# ⚠ BAD PRACTICE EXAMPLE (DO NOT USE)
# =====================================================================

new_car = Car("Tata", "Nano")

print(new_car.total_cars)  # ❌ Looks correct but:
# It accesses class variable indirectly through object
# Confusing + can accidentally create object-specific variable

print(Car.total_cars)  # ✔ Recommended


# ✔ Class variable shared across all objects → Same memory location
# ✔ Modify class variable using ClassName (not self)
# ✔ `self.variable` modifies only instance data (unique per object)
# ✔ Best use-case: counting objects, universal settings, etc.
# ✔ Access class variable using Car.total_cars → Good Practice
