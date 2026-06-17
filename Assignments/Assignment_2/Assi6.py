#calculate total salary of employee

DA = 10
TA = 12
HRA = 15

basic = int(input("Enter the basic salary: "))

#peform operations

DA = (DA/100)*basic
TA = (TA/100)*basic
HRA = (HRA/100)*basic

total_salary = basic + DA + TA + HRA

#Display the result

print(f'Total salary of employee is {total_salary}')