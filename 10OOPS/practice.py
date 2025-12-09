class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand
    def full_name(self):
         return f"The full name of the car is: {self.get_brand()} {self.model}"
    def fuel_type(self):
        return f"{self.model} is a disel car"


class ElectricCar(Car) :
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return f"{self.model} is a battery car"

my_car = Car("Tyota","ABC")
print(my_car.get_brand())
print(my_car.model)
print(my_car.full_name())
print(my_car.fuel_type())

my_car2 = Car("TATA","xyz")
print(my_car2.get_brand())
print(my_car2.model)
print(my_car2.full_name())
print(my_car2.fuel_type())


my_electric_car = ElectricCar("Tesla", "Model S", "75 kWh")
print(my_electric_car.get_brand())
print(my_electric_car.model)
print(my_electric_car.full_name())
print(my_electric_car.battery_size)
print(my_electric_car.fuel_type())

