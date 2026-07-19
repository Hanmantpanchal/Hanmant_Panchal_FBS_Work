#8. Write a program find reverse of a number
def revers(n):
    revers = 0 
    temp = n 
    while temp > 0:
        d = temp % 10
        revers = revers * 10 + d
        temp = temp // 10
    return revers

num = int(input("Enter a number : "))
print("Reverse of the number is : ",revers(num))