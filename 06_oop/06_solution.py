#6. Class Variables
#Problem: Add a class variable to Car that keeps track of the number of cars created.
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car+=1
class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize= batterySize
    def fuel_type(self):
            return "Electricity"

Car( "Toyota","Yaris")
Car( "Toyota","Camry")
ElectricCar("Tata","HarrierEV","70KW")

#print(my_car.total_car) this can also be used  to get the total number
print(Car.total_car)
