# =====================================================================
# 🔐 ENCAPSULATION IN PYTHON — BEST EXPLANATION
# =====================================================================
# ✔ Encapsulation = Hiding internal data and allowing controlled access
# ✔ Protects data from accidental modification
# ✔ Python uses:
#       _var  → Protected (convention)
#       __var → Private (name mangling done internally)
# =====================================================================


# 📌 We want to hide the brand attribute → make it private
class Car:
    def __init__(self, brand, model):
        self.__brand = brand     # private attribute
        self.model = model       # public attribute

    # Getter method → to safely access private attribute
    def get_brand(self):
        return self.__brand


# ✨ Creating object
my_car = Car("Toyota", "Camry")


# ❌ Direct access not allowed → Encapsulation protection
# print(my_car.brand) 
# AttributeError: 'Car' object has no attribute 'brand'

# ✔ Correct way — Access using getter
print(my_car.get_brand())



# ✔ Encapsulation hides sensitive data from outside access
# ✔ Private variable created using __ (double underscore)
# ✔ Can only be accessed using getter or setter
# ✔ Internally private names change → _ClassName__variable
#      Example: my_car._Car__brand  # not recommended!
