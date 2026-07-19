# c. 1^1 + 2^2 + 3^3+ ...... n^n

# def series(n):
#     sum = 0
#     count = 0 
#     for i in range(1 , n+1):#1 - 4 #2-4 #3-4 #4-4
#         for i in range(1 , i+1):#1-1 #1-2 #1-3 #1-4
#             count = count + 1#1#
            
#             sum = sum + i**count#1#
#         count = 0 
#     return sum
# num = int(input("Enter a number : "))
# print("sum of series is : ",series(num))


def series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i ** i

    return total

num = int(input("Enter a number: "))
print("Sum of series is:", series(num))