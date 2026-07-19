#9. Write a program to check if entered number is a palindrome or not.
def revers(n):
    revers = 0 
    temp = n 
    while temp > 0:
        d = temp % 10
        revers = revers * 10 + d
        temp = temp // 10
    if revers == n: 
        return revers
        
    else:
        print("Not a Palindrome")
    

num = int(input("Enter a number : "))
if revers(num) == num:
    print("It is a palindrome number :",revers(num))
