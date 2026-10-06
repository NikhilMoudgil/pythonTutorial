#7. Function with *args
#Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):# here *args is used to get multiple arguments 
    #print(args)-> it gives tuple
    return sum(args)
    
print(sum_all(1,2))
print(sum_all(1,2,3,4,5,6,7,8,9))