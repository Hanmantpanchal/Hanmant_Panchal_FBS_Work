# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

#print count of digits in a number

n = int(input("Enter a number : ")) #take input from user
temp = n #store the input number in temp variable
count = 0 
total =0 
i=1

while(0<temp):
    temp = temp//10
    count = count+1
    i = i+1
temp = n
while(0<temp):
    d=temp%10
    total = total + d**count
    temp = temp//10
if(n==total):
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
        
         