#4. Encapsulation
#Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    #Getter to make it private
    def get_brand(self):
        # WE CAN  make private via adding underscore 
        return self.__brand+ " !"
    def full_name(self):
        return f"{self.__brand}{self.model}"

my_car =Car( "Toyota","Yaris")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())