#4. Sum of all odd numbers between 1 to n
def oddNumber(n):
    sum=0
    for i in range(1,n+1):
        if(i%2!=0):
            sum = sum + i
    return sum
num = int(input("enter the number :"))
print("sum of odd number series :",oddNumber(num))