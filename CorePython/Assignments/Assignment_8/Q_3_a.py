# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

#a) 1+ 2 + 3 + 4+..... + n

def sumofseries(n):
    sum = 0  
    i = 1
    while (i <= n):
        sum = sum + i
        i = i + 1
    return sum

num = int(input("Enter a number : "))
print("Sum of series is : ",sumofseries(num))