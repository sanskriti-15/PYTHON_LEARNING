# =====================================================================
# 🎭 POLYMORPHISM IN PYTHON — BEST EXPLANATION
# =====================================================================
# ✔ Poly = Many + Morph = Forms → Same method name, different behavior
# ✔ Child class overrides parent class method to provide its own output
# ✔ Achieved using Method Overriding in OOP
# =====================================================================


# Parent Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):  # Common method name
        return "Petrol or Diesel"  # Default fuel in parent



# Child Class → Overrides fuel_type()
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def fuel_type(self):   # Same method name → Different behavior!
        return "Electricity"



# Testing polymorphism
my_car = Car("Toyota", "Camry")
print(my_car.fuel_type())   # Output → Petrol or Diesel

my_new_car = ElectricCar("Tesla", "Model S")
print(my_new_car.fuel_type())  # Output → Electricity


# ✔ Polymorphism allows SAME method to behave DIFFERENTLY based on object type
# ✔ Parent method → fuel_type()
# ✔ Child method → overrides fuel_type() with its own logic
# ✔ Helps in flexibility and code reusability
# ✔ Common use in real-world:
#      Car (fuel_type) → Petrol, Diesel, Electric, Hybrid
