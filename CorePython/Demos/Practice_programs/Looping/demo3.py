##3. Count the Number of Digits in palindrome Number

number = int(input("Enter the value of N: "))

count_palindrome = 0
i = 1

while(i <= number):

    temp = i
    rev = 0

    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d

    if(rev == i):
        count_palindrome = count_palindrome + 1

    i = i + 1

print("Count of palindrome numbers is:", count_palindrome)



