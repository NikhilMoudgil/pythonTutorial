#Problem: Choose a mode of transportation based on the distance 
# (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
distance = float(input("Enter the distance in kilometers: "))   

if distance < 3:
    print("You should walk.")
elif 3 <= distance <= 15:
    print("You should ride a bike.")
else:
    print("You should take a car.")