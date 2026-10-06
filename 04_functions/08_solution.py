#8. Function with **kwargs
#Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
# kwargs is used to handle multiple named arguments and used as given
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="nikhil",age=23)