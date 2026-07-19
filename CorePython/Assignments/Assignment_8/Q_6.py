# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibonacci(n):
    a=-1
    b=1
    

    for i in range(1 , n+1):
        c= a+b
        if c>0:
            print(c)
        a=b
        b=c
num =int(input("enter the number :"))
print("fibonacci series in given range :")
fibonacci(num)
         
        
    