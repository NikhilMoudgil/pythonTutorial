#10. Multiple Inheritance
#Problem: Create two classes Battery and Engine, 
#and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
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

class Battery:
    def battery_info(self):
         return "This is 77 kwh Battery"
class Engine:
    def engine_info(self):
         return"It has 2.0 Litre V8 Enngine" 
class ElectricCarTwo(Battery,Engine,Car):
     pass

my_new_ev = ElectricCarTwo("Tesla","Model S")
print(my_new_ev.engine_info())
print(my_new_ev.battery_info())