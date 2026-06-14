#convert days into years , week , days 

days = int(input('enter tha days '))

#perform operation 

#years in given days 
Years = days // 360 

#weeks in given days

Remaining_days = days % 365


Weeks = Remaining_days // 7

daysAfterWeeks = Remaining_days % 7

#Display the result

print(f'years in given days are {Years} weeks in given days are {Weeks} and days after weeks are {daysAfterWeeks}')



