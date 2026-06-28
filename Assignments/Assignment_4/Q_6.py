#WAP to check if a number is prime or not 

n = int(input("enter the number : "))
count = 0 
i = 2
if n>=2:
    while(i<n):
        if n%i==0:
            count=1
        i=i+1
    if count==0:
        print("it is a prime number")
    else : 
        print("it is not a prime number")
else:
    print("invalid value ")   
        