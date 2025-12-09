# =====================================================================
# 🧬 INHERITANCE IN PYTHON — BEST EXPLANATION
# =====================================================================
# ✔ Inheritance allows a class (Child) to reuse features from another class (Parent)
# ✔ Avoids code duplication and increases reusability
# ✔ Child class gets access to:
#       • Parent class attributes
#       • Parent class methods
# =====================================================================



# 📌 Parent Class (Base Class / Super Class)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"The full name of the car is: {self.brand} {self.model}"



# 📌 Child Class (Derived Class / Sub Class)
class ElectricCar(Car):  # Inheriting Car class
    def __init__(self, brand, model, battery_size):
        # super() → Calls parent class constructor to reuse initialization
        super().__init__(brand, model)
        self.battery_size = battery_size  # New attribute added by child class



# 🧪 Creating an object of Child class
my_electric_car = ElectricCar("Tesla", "Model S", "75 kWh")

# Child object accessing Parent attributes & methods
print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.full_name())
print(my_electric_car.battery_size)


# ✔ child class automatically gets all parent methods & attributes
# ✔ super() calls parent constructor to avoid code duplication
# ✔ child class can have extra attributes (battery_size here)
# ✔ real-life: Car → ElectricCar / SportsCar / SUVCar
