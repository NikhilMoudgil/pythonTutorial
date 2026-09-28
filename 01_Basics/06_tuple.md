# Tuples
# basic
>>> car_type=("SUV","Coupe")
>>> car_type 
('SUV', 'Coupe')

# Concetenation of two tuples
>>> more_cars=("MPV","Sedan")
>>> all_cars= car_type +more_cars

>>> all_cars                     
('SUV', 'Coupe', 'MPV', 'Sedan')
# Conditionals
>>> if "Coupe" in all_cars:
...     print("I have a Coupe Car")
... 
I have a Coupe Car

# TO Unwrap Tuples using tuples

>>> car_type
('SUV', 'Coupe')
>>> (suv,coupe)=car_type
>>> suv 
'SUV'
# to Check type 
>>> type(car_type)
<class 'tuple'>