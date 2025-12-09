# =====================================================================
# 📌BASIC CLASS & OBJECT IN PYTHON
# =====================================================================
# ✔ class → Blueprint/template to create objects
# ✔ object/instance → Real world entity created from class
# ✔ __init__() → Constructor → Automatically runs when object is created
# ✔ self → Refers to the current object (used to access attributes)
# =====================================================================


class Car:
    # ---------------------------------------------------------------
    # __init__ method → initializes object attributes at creation time
    # self.brand and self.model are INSTANCE VARIABLES
    # They are different for every object created
    # ---------------------------------------------------------------
    def __init__(self, brand, model):
        self.brand = brand   # Storing user value inside object
        self.model = model   # Storing user value inside object
        

# ---------------------------------------------------------------
# Creating first object of Car class
# Object has its own brand + model values
# ---------------------------------------------------------------
my_car = Car("Toyota", "Camry")
print(my_car.brand)   # Output: Toyota
print(my_car.model)   # Output: Camry
print("\n")


# ---------------------------------------------------------------
# Creating second object → totally separate from first object
# Shows different data for different instances
# ---------------------------------------------------------------
my_new_car = Car("Ford", "Mustang")
print(my_new_car.brand)   # Output: Ford
print(my_new_car.model)   # Output: Mustang


# =====================================================================
# FINAL NOTES (write in notebook)
# =====================================================================
# ✔ class defines structure → object stores actual data
# ✔ __init__ automatically runs when object is created
# ✔ self connects attributes to the current object
# ✔ Each object has independent data stored in separate memory
# =====================================================================
