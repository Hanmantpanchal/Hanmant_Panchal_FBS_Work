#find the sum of three digits 

num = int(input("enter the number :"))

#perform the operation

a= num%10
num= num//10

b= num%10
num= num//10

c= num%10
num= num//10

sum = a+b+c

#Display the result
print(sum)

