marks = int(input("Enter your marks: "))
if marks>100 or marks<0:
    print("Invalid marks")
    exit();
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
else:
    print("Grade F")