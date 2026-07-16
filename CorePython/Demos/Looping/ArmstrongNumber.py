#program to print armstrong number 

num = int(input("enter the number : "))
temp=num
count=0
sum = 0
while(temp>0):
    temp = temp//10
    count = count+1

temp=num
while(temp>0):
    d=temp%10
    sum = sum + d ** count
    temp = temp // 10
if(sum == num):
    print("armstrong number")
else:
    print("not armstrong number")


    
   
    
     