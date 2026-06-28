#WAP to print fibonacci series upto nth term

n=int(input("enter the value of n:"))
i = 1
a = -1
b=1

while i<=n:
    c=a+b
    a=b
    b=c
    i=i+1  
    print(c)
