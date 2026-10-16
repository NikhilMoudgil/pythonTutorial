#3. Inheritance
#Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand  }{  self.model}"
#Inheritance -> it has access to class Car using keyword Super()
class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize= batterySize
my_ev=ElectricCar("Tata","HarrierEV","70KW")
my_car =Car( "Toyota","Yaris")
print(my_car.full_name())
print(my_ev.brand,"  ",my_ev.model,"  ",my_ev.batterySize)
print(my_ev.full_name())