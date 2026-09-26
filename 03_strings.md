# Strings basic
marvel ="Comic SuperHero"
>>> marvel
'Comic SuperHero'
//String also be treated as the list
*first character/element
>>> firstchar=marvel[0]
>>> print(firstchar)   
C
#  Slicing 
'Comic SuperHero'
>>> slice_marvel =marvel[0:5]
>>> print(slice_marvel)         
Comic
>>> num_list ="0123456789"
>>> num_list[:]           
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
//additional third  parameter to tell how much steps to hop
>>>num_list[0:5:2]
'024'

# String Methods
>>> marvel               
'Comic Books'
>>> print(marvel.lower())
comic books
>>> print(marvel.upper())
COMIC BOOKS
* strip method- removes spaces from starting and endinh of the strings
>>> marvel="  Comic Books    "              
>>> marvel                    
'  Comic Books    '
>>> print(marvel.strip())
Comic Books
* replace is method to replace part of it
>>> marvel ="Fantastic Four"
>>> print(marvel.replace("Four","Two")) 
Fantastic Two

* String to list conversion -> Split
>>> marvel ="FantasticFour, UltimateSpiderMan , Avengers , Eternals"
>>> print(marvel.split(", "))          
['FantasticFour', 'UltimateSpiderMan ', 'Avengers ', 'Eternals']

* Find() method 
>>> F1 = "Formula One"
>>> F1
'Formula One'
>>> print(F1.find("One"))
8 