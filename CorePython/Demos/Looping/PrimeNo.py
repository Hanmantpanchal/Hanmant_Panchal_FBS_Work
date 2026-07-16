#write a programm to print prime number 

n = int(input("enter the number "))
flag = 0

for i in range(2,n):
    if n%i==0:
        flag = 1
        break
if flag==0:
    print("it is a prime number")
else:
    print("it is not prime number ")


