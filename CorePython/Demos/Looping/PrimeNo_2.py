#WAP to print prime number using else 

n = int(input("enter the number :"))
flag = 0

for i in range(2,n):
    if(n%i==0):
        flag==1