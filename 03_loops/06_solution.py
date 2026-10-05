#Problem: Compute the factorial of a number using a while loop.
number = int(input("Enter a number: "))
factorial = 1
i=1
while i<=number:
    factorial *=i
    i+=1
print(f"The factorial of {number} is: {factorial}")