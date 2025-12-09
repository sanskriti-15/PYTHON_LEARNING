# =====================================================================
# 📌CLASS INHERITANCE + isinstance() FUNCTION
# =====================================================================
# ✔ Inheritance → Create a new class based on an existing class
# ✔ Helps reuse code (attributes + methods)
# ✔ Child class can add extra properties of its own
# =====================================================================


# ------------------------------
# 🅿️ Parent Class (Base Class)
# ------------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand    # attribute from parent
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


# ------------------------------
# 🧬 Child Class (Derived Class)
# ------------------------------
class ElectricCar(Car):  # Inheriting from Car
    def __init__(self, brand, model, battery_size):
        # super() → calls parent class constructor
        super().__init__(brand, model)
        self.battery_size = battery_size  # New attribute added by child class


# ------------------------------
# 🎯 Creating object of Child class
# ------------------------------
my_electric_car = ElectricCar("Tesla", "Model S", "75 kWh")

print(my_electric_car.brand)         # inherited attribute
print(my_electric_car.model)         # inherited attribute
print(my_electric_car.full_name())   # inherited method
print(my_electric_car.battery_size)  # child class attribute


# =====================================================================
# 🔍 isinstance() FUNCTION — TYPE CHECKING TOOL
# =====================================================================
# ✔ Checks if a given object belongs to a specific class
# ✔ Returns Boolean True / False
# =====================================================================

print(isinstance(my_electric_car, ElectricCar))  # ✔ True → It is ElectricCar
print(isinstance(my_electric_car, Car))          # ✔ True → It is also Car (because of inheritance)
print("\n")

print(isinstance(ElectricCar, Car))  # ❌ False → Class is not an instance of another class


# =====================================================================
# FINAL NOTES (To write)
# =====================================================================
# ✔ Inheritance → Code reusability (child gets all of parent)
# ✔ super() → Calls parent constructor inside child
# ✔ isinstance(object, Class) → Checks object’s class type
# ✔ Child class object is always instance of:
#       - Its own class
#       - Its parent class
# ❌ Class itself is not an instance of another class
# =====================================================================
