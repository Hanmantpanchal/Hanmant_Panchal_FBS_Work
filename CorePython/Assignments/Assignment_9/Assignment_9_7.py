#7. Write a program to find sum of digits using recursion.
def sumofDigit(num):
    if num == 0:
        return 0
    else:
        return (num%10) + sumofDigit(num//10)
n = int(input("Enter a number : "))
print(sumofDigit(n))
