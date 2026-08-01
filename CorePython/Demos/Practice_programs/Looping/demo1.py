# Check Palindrome Number

num = int(input("Enter the number: "))

temp = num
rev = 0

while temp > 0:
    d = temp % 10        # Get the last digit
    temp = temp // 10    # Remove the last digit
    rev = rev * 10 + d   # Build the reversed number

if rev == num:
    print("It is a palindrome")
else:
    print("It is not a palindrome")