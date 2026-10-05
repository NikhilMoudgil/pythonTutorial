#1. Counting Positive Numbers
#Problem: Given a list of numbers, count how many are positive.
number = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
is_positive = 0
for n in number:
    if n > 0:
        print(f"{n} is a positive number.")
        is_positive += 1
print(f"Total positive numbers: {is_positive}")