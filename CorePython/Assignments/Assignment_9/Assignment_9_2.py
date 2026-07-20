#2. Write a program to check if given number is Armstrong or not using recursive function.
# Count the number of digits recursively
def numberCount(num):
    if num == 0:
        return 0
    return 1 + numberCount(num // 10)

# Calculate Armstrong sum recursively
def Armstrong(n, digits):
    if n == 0:
        return 0
    return (n % 10) ** digits + Armstrong(n // 10, digits)

# Input
num = int(input("Enter a number: "))

# Handle 0 separately
if num == 0:
    digits = 1
else:
    digits = numberCount(num)

# Check Armstrong
if Armstrong(num, digits) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")