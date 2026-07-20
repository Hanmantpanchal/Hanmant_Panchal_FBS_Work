#4. Write a program to find sum of n numbers using recursion.

def sumofn(num):
    if num == 0:
        return 0
    else:
        return num + sumofn(num-1)


num = int(input("Enter a number : "))
print(sumofn(num))