# Numbers in Python
>>> x= 2
>>> y=3
>>> z=4
>>> x+y
5
>>> y**x//power
9
>>> 
//precedence
>>> (x+y)*z
20
//precision
>>> 40+2.32 //bad work
42.32 

// DataType
>>> int(2.36)
2
>>> float(10)
10.0
>>>
# Operator Overloading 
>>> 'nikhil' + 'Moudgil'
'nikhilMoudgil'

* when we call multiple variables it gives values as tuples
>>> x,y,z
(2, 3, 4)

//modulus
>>> y%2
1
//power
>>> z**2
16
//Excepion with python it can calculate with  large precision
>>> 2**1000  
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

//Best Results with precision formating 
>>> result =1/3.0
>>> result
0.3333333333333333

# repr() function in python ->  the repr() built-in function returns an unambiguous, developer-friendly string representation of an object

>>> repr('Nikhil')
"'Nikhil'"
>>> str('nikhil')
'nikhil'
>>> print('nikhil')
nikhil //difference in results

# Comparison -> 
 * fact -> true and false in python are actual 0 and 1 but repr tend them to become True And False
>>> 1<2
True
>>> 1>2
False
//comparison 
>>> x<y<z
True
>>> x<y and y<z
True
//In given expression the values looks common
True
>>> 1 == 2<3
False
>>> 1 == 2 and 2<3 
False
# Math Library 
//floor -> it gives bottom value
>>> import math
>>> math.floor(3.5)
3
>>> math.floor(-3.5)
-4
>>> math.floor(3.6) 
3
//trunc takes us towards zero
>>> math.trunc(3.6)
3
>>> math.trunc(2.8)
2
 # Complex NUmbers
>>> (2+1j)*3
(6+3j)

//Octal Number
>>> 0o20
16
//hexaDecimal
>>> 0xff
255
//binary 
>>> 0b1000
8
# Conversion Function in python
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'
//With Integer
* to octal
>>> int('64',8)
52
*to binary
>>> int('1000',2)
8
* to hexadecimal
>>> int('1000',16)
4096
# Bitwise Operations
>>> x << 2
4 //leftshift by 2
>>> x >>  2
0 //rightshift by 2

#random library
>>> random.random() 
0.21111413416893476
 
* randint()->
 >>> random.randint(1,10)  
3
>>> random.randint(1,10)
9
>>> random.randint(1,10)
10
>>> random.randint(1,10)
10
* Random Choice 
>>> l1 =['DC','Marvel','Anime']
>>> random.choice(l1)
'DC'
>>> random.choice(l1)
'Marvel'
>>> random.choice(l1)
'DC'
>>> random.choice(l1)
'Marvel'
* Shuffle() function ////IN card games such as problem
>>> l1 =['DC','Marvel','Anime','Kdrama']
>>> random.shuffle(l1)
>>> l1                
['Marvel', 'Kdrama', 'DC', 'Anime']
>>> random.shuffle(l1)
>>> l1                
['Kdrama', 'Marvel', 'DC', 'Anime']

# Decimal Library 
from decimal import Decimal
>>> Decimal('0.1')+ Decimal('0.1')+ Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1')+ Decimal('0.1')- Decimal('0.1')
Decimal('0.1')
# from fractions import Fraction 
>>> myfraction =Fraction(2,7)
>>> myfraction
Fraction(2, 7)

# Sets 
>>> setone ={1,2,3,4}
>>> setone
{1, 2, 3, 4}
//Set Intersection
>>> setone & {1,3}   
{1, 3}
//Union
>>> setone | {1,3}
{1, 2, 3, 4}
* Empty Set 
>>> setone-{1,2,3,4}
set() //as {} is dictionary

# Boolean
>>> type(True)
<class 'bool'>
>>> True == 1
True
//True is treated as 1
>>> True+4    
5