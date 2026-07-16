#program to print palindrome number in using while loop

num = int(input("enter the number :"))
temp = num
rev = 0
while(temp>0):
    d = temp % 10
    rev = rev * 10 + d
    temp = temp // 10
if(num == rev):
    print("palindrome")
else:
    print("not palindrome")
    