#print fibonacci series 

n=int(input("enter the number "))
a = -1
b = 1
for i in range(1, n+1):
    c = a+b 
    print(c)
    a=b
    b=c