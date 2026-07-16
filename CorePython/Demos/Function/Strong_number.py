def factorial(n):
   fact = 1
   for i in range(1 , n+1):
       fact = fact*i
   return fact
   
def isStrong(num):
    temp = num
    sum = 0
       
    while(temp>0):
        d = temp%10
        temp = temp//10
        fact = factorial()
        sum = sum+fact
    if sum == num :
        return True
    else:
        return False

number = int(input("enter the number :"))
f = isStrong(number)
print(f)   
        
        