#7. Write a program to find sum of digits of a number.
def digitSum(n):
    temp = n
    total = 0

    if n > 9:
        while temp > 0:
            d = temp % 10
            total = total + d
            temp = temp // 10
        return total
    else:
        print("It is a single-digit number. Number should be greater than 9.")

num = int(input("Enter the number: "))
print("Sum of digits:", digitSum(num))


