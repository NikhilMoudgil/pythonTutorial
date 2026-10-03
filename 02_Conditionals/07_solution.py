#Problem: Customize a coffee order: 
# "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
size = input("Enter the coffee size (Small/Medium/Large): ").lower()
extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").lower()     
if size not in ["small", "medium", "large"]:
    print("Invalid size. Please choose Small, Medium, or Large.")   
elif extra_shot not in ["yes", "no"]:
    print("Invalid input for extra shot. Please answer with 'yes' or 'no'.")    
else:
    order = f"You ordered a {size.capitalize()} coffee"
    if extra_shot == "yes":
        order += " with an extra shot of espresso."
    else:
        order += "."
    print(order)