#4. Function Returning Multiple Values
#Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math
def circle_stats(radius):
    area=  round(math.pi*radius **2,2)
    circumference=round(2*math.pi*radius,2)# round function for rounding off two pricision
    return area ,circumference


a,c=circle_stats(2) # a and c are here for handling two values of function

print("Area",a," Circumference",c)