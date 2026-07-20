#1. Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +….. + n!
# Note : For fact and sum two recursive functions

# Recursive function to find factorial
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

# Recursive function to find sum of the series
def sumofSeries(n):
    if n == 1:
        return fact(1)
    return fact(n) + sumofSeries(n - 1)

number = int(input("Enter a number: "))
print("Sum =", sumofSeries(number))