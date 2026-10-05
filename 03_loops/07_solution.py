#7. Validate Input
#Problem: Keep asking the user for input until they enter a number between 1 and 10.

from sympy import true
while true :
    
   number =int(input("Enter a number: "))
   if 1<= number  <= 10:
       print(f"You entered a valid number: {number}")
       break
   print("Invalid input. Please enter a number between 1 and 10.")
   number = int(input("Enter a number: "))
   
