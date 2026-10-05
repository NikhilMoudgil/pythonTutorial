#Problem: Given a string, find the first non-repeated character.
import string
str = input("Enter a string: ")
for char in str:
    if  str.count(char)==1:
        print("The first non-repeating character is:", char)
        break