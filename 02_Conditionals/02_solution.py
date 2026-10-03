UserAge= int(input("Give me An Age of User:"))
showDay=input ("What is the day of show: ")
print("Age Of the User = ",UserAge)
print("Day Of the Show = ",showDay)
ticketPrice=()
if UserAge<18:
     ticketPrice=8
else :
     ticketPrice=12

if showDay== "Wednesday":
    ticketPrice-=2
    print("$",ticketPrice," is the ticket price applying discounts")
else:
    print("$",ticketPrice," is the ticket Price")