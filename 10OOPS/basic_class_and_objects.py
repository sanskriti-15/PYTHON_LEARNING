# =====================================================================
# 📘 CLASS IN PYTHON — BLUEPRINT FOR CREATING OBJECTS
# =====================================================================
# ✔ Class contains Attributes + Methods
# ✔ Object is an instance created from a Class
# ✔ __init__() works as a constructor → initializes object variables
# ✔ self refers to the current object (context of object instance)
# =====================================================================


class user_login:

    # Constructor → runs automatically while creating object
    def __init__(self, username, email, password):
        self.username = username    # instance attribute
        self.email = email
        self.password = password

    # Method → uses object data through `self`
    def hashed_password(self):
        return f"{self.password}#$%^&"    # fake hashing for demo

    def username_uppercase(self):
        return self.username.upper()


# Creating an object → calling constructor
login = user_login("john", "john@me.com", "1234")

print(login.username)        # accessing attribute
print(login.email)
print(login.password)
print(login.hashed_password())     # calling method
print(login.username_uppercase())
print("\n")


# Checking types
print(type(login))           # <class '__main__.user_login'>
print(type(login.username))  # <class 'str'>
print("\n")
