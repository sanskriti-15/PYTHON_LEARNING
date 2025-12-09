# =====================================================================
# 🏷️ PROPERTY DECORATORS — BEST EXPLANATION
# =====================================================================
# ✔ Used to turn a method into a READ-ONLY attribute
# ✔ Helps implement Encapsulation (private variables: __var)
# ✔ Prevents accidental modification from outside the class
# ✔ Eliminates the need to call getter_method() explicitly
# =====================================================================


class Car:
    def __init__(self, brand, model):
        self.__brand = brand     # private attribute
        self.__model = model     # private attribute

    # 🎯 Getter using @property
    @property
    def model(self):
        return self.__model    # Now model behaves like a normal attribute



# Creating object
car1 = Car("Honda", "Civic")

print(car1.model)  # ✔ Calling without () like an attribute


# ❌ Trying to modify → NOT allowed (Read-Only)
# car1.model = "Accord"
# AttributeError: property 'model' of 'Car' object has no setter

# ✔ To protect data from unwanted modifications
# ✔ To provide controlled, secure access to private attributes
# ✔ To use method like an attribute (no parentheses)
