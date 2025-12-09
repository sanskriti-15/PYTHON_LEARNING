# =====================================================================
# 📌MULTIPLE INHERITANCE IN PYTHON
# =====================================================================
# ✔ Multiple Inheritance → A class inherits from MORE THAN ONE parent class
# ✔ This allows combining features from multiple classes into one
# ✔ In Python, order of inheritance matters (MRO → Method Resolution Order)
# =====================================================================



# ------------------------------
# 🅿️ Parent Class 1
# ------------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# ------------------------------
# 🅿️ Parent Class 2
# ------------------------------
class Battery:
    def battery_size(self):
        return "The car has a battery size of 100kWh"


# ------------------------------
# 🅿️ Parent Class 3
# ------------------------------
class Engine:
    def engine_size(self):
        return "The car has an engine size of 2000cc"



# ---------------------------------------------------------------------
# 🔋⚙️ Child Class → Multiple Inheritance
# ---------------------------------------------------------------------
# ✔ Inherits from Car, Battery, Engine
# ✔ Can access attributes & methods from all parents
# ---------------------------------------------------------------------
class ElectricCar(Car, Battery, Engine):
    pass



# 📌 Creating an instance of child class
E_car = ElectricCar("Tesla", "Model S")

# Accessing everything inherited from multiple parents
print(E_car.brand)          # From Car
print(E_car.model)          # From Car
print(E_car.battery_size()) # From Battery
print(E_car.engine_size())  # From Engine


# =====================================================================
# FINAL NOTES (Write these)
# =====================================================================
# ✔ Multiple Inheritance enables combining multiple features into one class
# ✔ If multiple parents have same method name → Python uses MRO
#    (Method Resolution Order → left-to-right order in class definition)
# ✔ Class ElectricCar inherits from Car → Battery → Engine in this exact order
# ✔ Useful for mixin classes (additional reusable behavior)
# =====================================================================
