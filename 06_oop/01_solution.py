#1. Basic Class and Object
#Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
# Class name are always Capitalized and since we have class and context of class it can we used by any variable
#__init__ is a constructor is a method ,when any object is created by class called 
class Car:
   # brand=None -> this will not give us result there  is a syntax for this 
    #model=None
    def __init__(self,brand,model): # syntax for creating function in class
        self.brand=brand
        self.model=model
# given variable try to access class Car using keyword self it establishes connection with class


my_car =Car( "Toyota","Yaris")
print(my_car.brand)
print(my_car.model)

my_car2=Car("Suzuki","Ciaz")
print(my_car2.brand)