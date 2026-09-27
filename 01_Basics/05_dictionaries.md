# Dictionaries -> Key : Value
>>> car_type ={"SUV":"ScorpioN","Sedan":"Mercedes S Class","Coupe":"Urus"}
>>> car_type                                                              
{'SUV': 'ScorpioN', 'Sedan': 'Mercedes S Class', 'Coupe': 'Urus'}
# Fetch Value from key
>>> car_type["SUV"]
'ScorpioN'

# Methods

* get() method
>>> car_type.get("Coupe")
'Urus'

# Changing Values
>>> car_type["SUV"]="Harrier"
>>> car_type                 
{'SUV': 'Harrier', 'Sedan': 'Mercedes S Class', 'Coupe': 'Urus'}

# Iteration In Dictionary (Introduction only)
// keys only
{'SUV': 'Harrier', 'Sedan': 'Mercedes S Class', 'Coupe': 'Urus'}
>>> for car in car_type:
...     print(car)
... 
SUV
Sedan
Coupe 
// key value pair
{'SUV': 'Harrier', 'Sedan': 'Mercedes S Class', 'Coupe': 'Urus'}
>>> for car in car_type:
...     print(car,car_type[car])
... 
SUV Harrier
Sedan Mercedes S Class
Coupe Urus
//Another syntax for iteration/loop using items
>>> for key,value  in car_type.items():
...     print(key,value)               
... 
SUV Harrier
Sedan Mercedes S Class
Coupe Urus

# Conditional in Dictionary 
>>> if "SUV" in car_type:         
...     print("I have an SUV car")
... 
I have an SUV car

# pop() method // remove the given item/pair given as
>>> car_type.pop("Sedan")
'Mercedes S Class'
>>> car_type             
{'SUV': 'Harrier', 'Coupe': 'Urus', 'HatchBack': 'PoloGT'}

# popitem() //removes the item at last
>>> car_type.popitem()       
('HatchBack', 'PoloGT')
>>> car_type          
{'SUV': 'Harrier', 'Coupe': 'Urus'}

# del keyword // it delete referance from memory as well
>>> del car_type["Coupe"]  
>>> car_type
{'SUV': 'Harrier', 'HatchBack': 'PoloGT', 'Sedan': 'S Class'}

# copy dictionary
>>> car_type_copy =car_type.copy()
>>> car_type_copy
{'SUV': 'Harrier', 'HatchBack': 'PoloGT', 'Sedan': 'S Class'}

# nested Dictionaries
>> car_showroom ={
... "car":{"SUV":"Harrier","Sedan":"VirtusGT"},
... "Bike":{"Trail":"XPulse","Touring":"Meteor"}
... }
>>> car_showroom   
{'car': {'SUV': 'Harrier', 'Sedan': 'VirtusGT'}, 'Bike': {'Trail': 'XPulse', 'Touring': 'Meteor'}}

# Extracting item from Nested Dictionary
>>> car_showroom["car"]  
{'SUV': 'Harrier', 'Sedan': 'VirtusGT'}
//particular Item
>>> car_showroom["car"]["Sedan"]
'VirtusGT'

# Dictionary Comprehension
>>> square_num={x:x**2 for x in range(6)}
>>> square_num                           
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Clear() Method
square_num.clear()
>>> square_num        
{}

# Dictionary Construction from arrays using constructor dist.

>>> key =["SUV","Sedan","Coupe"]
>>> default_value ="Vehicle"
// default value for each key 
>>> new_dict = dict.fromkeys(key ,default_value)     
>>> new_dict                                    
{'SUV': 'Vehicle', 'Sedan': 'Vehicle', 'Coupe': 'Vehicle'}