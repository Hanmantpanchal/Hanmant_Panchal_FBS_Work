#5. Write a program to find factorial using recursion.
def sumofFact(num):
    if num == 0:
        return 1
    else:
        return num * sumofFact(num - 1)
    

num = int(input("Enter a number : "))
print(sumofFact(num))