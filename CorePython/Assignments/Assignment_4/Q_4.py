#WAP to print factorial of a number
n=int(input("enter the value of n:"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i=i+1
print("factorial of",n,"is",fact)