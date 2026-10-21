#7. Static Method
#Problem: Add a static method to the Car class that returns a general description of a car.
#A static method in Python is a method defined inside a class that does not require an instance of the class to be called.
#It is created using the @staticmethod decorator and behaves exactly like a regular function, except it lives inside the class's
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
ElectricCar("Tata","HarrierEV","70KW")


#print(mycar.general_description()) -> this will give error as try to access via object and it is static method
print(Car.general_description())