#13. Write a program to input electricity unit charges and calculate total electricity bill
#according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

unit=int(input("Enter the unit:"))
if (unit<=50):
    bill=unit*0.50
    surcharge = (20/100)*bill
    total_bill = bill + surcharge
    print("Total bill is:",total_bill)
elif (unit>=51 and unit<=150):
    bill=unit*0.75
    surcharge = (20/100)*bill
    total_bill = bill + surcharge
    print("Total bill is:",total_bill)
elif (unit>=151 and unit<=250):
    bill=unit*1.20
    surcharge = (20/100)*bill
    total_bill = bill + surcharge
    print("Total bill is:",total_bill)
else:
    bill=unit*1.50
    surcharge = (20/100)*bill
    total_bill = bill + surcharge
