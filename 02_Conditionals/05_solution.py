#Problem: Suggest an activity based on the weather 
# (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("Enter the weather condition (Sunny/Rainy/Snowy): ").lower()
if weather == "sunny":
    print("It's a great day for a walk!")
elif weather == "rainy":
    print("Perfect time to read a book indoors.")
elif weather == "snowy":
    print("Let's build a snowman!")
else:
    print("Weather condition not recognized. Please enter Sunny, Rainy, or Snowy.")