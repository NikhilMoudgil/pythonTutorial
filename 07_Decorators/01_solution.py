#Problem 1: Timing Function Execution
#Problem: Write a decorator that measures the time a function takes to execute.

import time
# for decorators we need to follow syntax then we have to create the function inside the function  
def timer(func):
    def wrapper(*args,**kwargs):
      start = time.time()
      result =func(*args , **kwargs)
      end = time.time()
      print(f"{func.__name__}ran in {end-start} time")
      return result
    return wrapper
@timer # decorated via timer and always pass through timer
def example_function(n):
   time.sleep(n)
example_function(2)