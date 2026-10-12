# Global Scope And Function Scope and Usually Declared By the Indentation
#Example 1
username = "John"  # Global variable

def func():
    username = "Alice"  # Local variable
    print(username)  # Output: Alice
print(username)  # Output: John
#here the scope of the variable username is global, so it prints "John" instead of "Alice" 
# which is defined inside the function func.
func()

#Example 2
x = 99#global variable
def func2(y):
    z=x+y
    return z
result= func2(1)  # Output: 100
print(result)  # Output: 100

# Example 3
def func3():
    global x  # Declare x as a global variable
    x=200 # It is a bad practice we dont have to overwrite the global variables
func3()
print(x) 

#Example 4
def f1():
    x=88
    # It is function inside a function  and if x is not available in function 
    # then it will access the gloabal variable x 
    def f2():
        print(x)
    return f2() 
myresult=f1()

#Example 5 - closure/factory function
def nikhilbuilds(num):
    def actual(x):
        return x**num
    return actual

f=nikhilbuilds(2)
g=nikhilbuilds(3)
print(f(3))
print(g(3))
#These are Example of closure in Python