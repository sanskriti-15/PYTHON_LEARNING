# =====================================================================
# 🧊 STATIC METHOD IN PYTHON — BEST EXPLANATION
# =====================================================================
# ✔ A static method belongs to the CLASS, not to any specific object
# ✔ It does NOT need:
#        - self (object reference)
#        - cls (class reference)
# ✔ Behaves like a normal function inside a class for organization
# ✔ Used when logic is related to class but doesn't access class data
# =====================================================================


class Car:
    total_cars = 0   # Class variable → shared by all cars

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1  # Counting objects created

    # Getter method for private attribute
    def get_brand(self):
        return self.__brand
    

    # 🚀 STATIC METHOD  (self is not written)
    @staticmethod
    def general_description():
        return "Cars are prime transport vehicles."
    

# Creating object
myCar = Car("Toyota", "Camry")

print(myCar.general_description())  # Allowed ✔ (not recommended)
print(Car.general_description())    # Recommended ✔✔✔



# ---------------------------------------------------------------------
# Inheritance + Static Method
# ---------------------------------------------------------------------
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity


e_car_01 = ElectricCar("Tesla", "Model S", "100 kWh")

print(e_car_01.general_description())  # ✔ Inherited by child class


# ✔ @staticmethod does NOT take self or cls
# ✔ Can be called using ClassName or Object reference
# ✔ Good for utility/helper functions inside a class
# ✔ Static methods are inherited by child classes
# ✔ They do NOT modify object or class level data
