#compound Intrest

Principle = int(input("enter value of principle :"))
Time = int(input("enter value of time :"))
Rate = int(input("enter the rate :"))


#perform operation

A = Principle * (1+Rate/100)**3

CI= A-Principle

#Display the result

print(f'compound intrest is {CI}')

