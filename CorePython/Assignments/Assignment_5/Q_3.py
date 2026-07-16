# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
passenger = int(input("Enter the number of passengers: "))
ticket_price = int(input("Enter the ticket price: "))

i = 1
total_amount = 0

while(i <= passenger):
    print(f"Passenger {i}")

    age = int(input(f"Enter the age of passenger {i}: "))

    if age < 12:
        amount = ticket_price - (ticket_price * 30 / 100)
        print(f"30% discount applied.")
    elif age > 59:
        amount = ticket_price - (ticket_price * 50 / 100)
        print(f"50% discount applied.")
    else:
        amount = ticket_price
        print("No discount.")

    print(f"Ticket Amount = {amount}")

    total_amount += amount

    i += 1

print(f"Total Ticket Amount = {total_amount}")