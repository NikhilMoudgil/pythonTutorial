#8. Property Decorators
#Problem: Use a property decorator in the Car class to make the model attribute read-only.
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1
#Decorators
    #Static method
    @staticmethod
    def general_description():
         return "Cars are machine to transport but more than that for men they are thier love"
    @property
    def model(self):
         return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize= batterySize

    def fuel_type(self):
            return "Electricity"

mycar=Car( "Toyota","Yaris")
#mycar.model="Corrola" try to change the model 
print(mycar.model)

Car( "Toyota","Camry")
ElectricCar("Tata","HarrierEV","70KW")

