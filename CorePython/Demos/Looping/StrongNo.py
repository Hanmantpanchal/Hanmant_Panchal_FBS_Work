#WAP to print number is strong or not 


n = int(input("Enter the number : "))
temp  = n 
sum = 0 
i = 1

while(temp>0):
    d = temp%10
    fact = 1
    for i in range(1,d+1):
        fact = fact * i
    sum = sum + fact 

    temp = temp // 10

if sum == n:
    print("it is strong number ")
else :
    print("it is not strong number ")


    

