#11. Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

age1 = int(input("Enter age of first person: "))
age2 = int(input("Enter age of second person: "))
age3 = int(input("Enter age of third person: "))
age4 = int(input("Enter age of fourth person: "))
age5 = int(input("Enter age of fifth person: "))

ticket = int(input("Enter ticket amount per person: "))

total = 0

# Person 1
if(age1 < 12):
    total =total + ticket - (ticket * 30 / 100)
elif(age1 > 59):
    total =total + ticket - (ticket * 50 / 100)
else:
    total= total +ticket

# Person 2
if(age2 < 12):
    total= total + ticket - (ticket * 30 / 100)
elif(age2 > 59):
    total= total + ticket - (ticket * 50 / 100)
else:
    total=total + ticket

# Person 3
if(age3 < 12):
    total =total + ticket - (ticket * 30 / 100)
elif(age3 > 59):
    total= total + ticket - (ticket * 50 / 100)
else:
    total= total +ticket

# Person 4
if(age4 < 12):
    total= total + ticket - (ticket * 30 / 100)
elif(age4 > 59):
    total= total + ticket - (ticket * 50 / 100)
else:
    total= total + ticket

# Person 5
if(age5 < 12):
    total= total + ticket - (ticket * 30 / 100)
elif(age5 > 59):
    total= total + ticket - (ticket * 50 / 100)
else:
    total= total + ticket

print("Total Ticket Amount =", total)