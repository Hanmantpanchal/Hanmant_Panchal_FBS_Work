def palindrome(num):
    temp = num
    rev = 0
    while(temp>0):
        d = temp%10
        temp = temp//10
        rev = rev*10 + d
        
    if rev == num:
        return True
    else:
        return False
    

num = int(input("enter the number :"))
res = palindrome(num)
print(res)