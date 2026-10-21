#5. Polymorphism
#Problem: Demonstrate polymorphism by defining a method fuel_type in 
#both Car and ElectricCar classes, but with different behaviors.
#IN given example we take two objects and access same method but get different values
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand}{self.model}"
    def fuel_type(self):
        return "Petrol or Diesal"
class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize= batterySize
    def fuel_type(self):
            return "Electricity"

my_car =Car( "Toyota","Yaris")
print(my_car.fuel_type())
my_ev=ElectricCar("Tata","HarrierEV","70KW")
print(my_ev.fuel_type())
