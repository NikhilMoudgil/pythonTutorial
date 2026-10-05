#Problem: Recommend a type of pet food based on the pet's species and age. 
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
species = input("Enter your pet's species (Dog/Cat): ").lower()
age = int(input("Enter your pet's age in years: "))  
if species not in ["dog", "cat"]:
    print("Invalid species. Please choose Dog or Cat.")
elif species =="dog":
    if age < 2:
        food = "Puppy food"
    elif 2 <= age <= 7:
        food = "Adult dog food"
    else:
        food = "Senior dog food"
elif species =="cat":
    if age < 1:
        food = "Kitten food"
    elif 1 <= age <= 5:
        food = "Adult cat food"
    else:
        food = "Senior cat food"    
else:
    food = "Unknown food type"