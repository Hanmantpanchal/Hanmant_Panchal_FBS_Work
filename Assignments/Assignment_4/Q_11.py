#11. WAP to check if given number Strong Number.

n=int(input("Enter a number : "))
i = 1
sum = 0 
temp=n
while(0<n):
    d=n%10
    fact=1
    k=1
    while(k<=d):
        fact=fact*k
        k = k+1
    sum = sum + fact

    n= n//10
    i= i+1
if(sum==temp):
    print(f"{temp } is a strong number")
else:
    print("it is not a strong number ")