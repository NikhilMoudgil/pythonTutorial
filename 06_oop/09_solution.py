#9. Class Inheritance and isinstance() Function
#Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car+=1
    #Static method
    @staticmethod
    def general_description():
         return "Cars are machine to transport but more than that for men they are thier love"
class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize= batterySize
    def fuel_type(self):
            return "Electricity"

mycar=Car( "Toyota","Yaris")
Car( "Toyota","Camry")
myev=ElectricCar("Tata","HarrierEV","70KW")
# check if myev is instance of classes Car and Electric Car using isinstance
print(isinstance(myev,Car))
print(isinstance(myev,ElectricCar))