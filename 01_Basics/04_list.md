# Lists 

>>> carVarieties =["Seedan","Coupe","SUV","HatchBack","CrossOver","MPV"]
>>> carVarieties                                                        
['Seedan', 'Coupe', 'SUV', 'HatchBack', 'CrossOver', 'MPV']

# Slicing
>>> print(carVarieties[-1])
MPV
>>> print(carVarieties[1:3])
['Coupe', 'SUV']
>>> print(carVarieties[2:]) 
['SUV', 'HatchBack', 'CrossOver', 'MPV']
>>> print(carVarieties[2:6:2])
['SUV', 'CrossOver']

# Make Changes directly on position
>>> carVarieties
['Seedan', 'Coupe', 'SUV', 'HatchBack', 'CrossOver', 'MPV']
>>> carVarieties[3]="CompactSUV"
>>> carVarieties                
['Seedan', 'Coupe', 'SUV', 'CompactSUV', 'CrossOver', 'MPV']

* Without Anything given it will give an empty list
>>> carVarieties              
['Seedan', 'Coupe', 'SUV', 'CompactSUV', 'CrossOver', 'MPV']
>>> print(carVarieties[1:1])  
[]
* Insert Nothing
>>> carVarieties              
['Seedan', 'Coupe', 'SUV', 'CompactSUV', 'CrossOver', 'MPV']//before
//after
>>> carVarieties[3:4]=[]    
>>> carVarieties        
['Seedan', 'Coupe', 'SUV', 'CrossOver', 'MPV']

# looping in list 
>>> for car in carVarieties:
...     print(car)
... 
Seedan
Coupe
SUV
CrossOver
MPV
* IF
>>>if "Coupe" in carVarieties:
...     print("I have Coupe Car")
... 
I have Coupe Car
# APPEND-> Appends in last of list

# pop() method -> removes last element 
>>> carVarieties            
['Seedan', 'Coupe', 'SUV', 'CrossOver', 'MPV']
>>> carVarieties.pop() 
'MPV'

# Inserting Something
>>> carVarieties.insert(1,"MPV")
>>> carVarieties                
['Seedan', 'MPV', 'Coupe', 'SUV', 'CrossOver']

//When a assign another list a list then it gets direct referance from memory as 
>>> carVarieties_copy=carVarieties
//so we use copy method as it will  assign the copy of values not actual memory refference
>>> carVarieties_copy=carVarieties
//the difference in two
>>> carVarieties_copy.append("CompactSUV")
>>> carVarieties_copy
['Seedan', 'MPV', 'Coupe', 'SUV', 'CrossOver', 'CompactSUV']
>>> carVarieties
['Seedan', 'MPV', 'Coupe', 'SUV', 'CrossOver']