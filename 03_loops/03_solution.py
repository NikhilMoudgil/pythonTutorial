number = int(input("Enter a number: "))
for i in range(1, 11):
    if i == 5:
        continue
    print(f"{number} X {i} = {number * i}")