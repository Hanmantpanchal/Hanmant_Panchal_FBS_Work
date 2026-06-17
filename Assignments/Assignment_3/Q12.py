#12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3 digit number: "))
temp = num

first_digit = num // 100 # 123 // 100 = 1
second_digit = (num // 10) % 10 # 123 // 10 = 12, 12 % 10 = 2
third_digit = num % 10 # 123 % 10 = 3 

reversed_num = (third_digit * 100) + (second_digit * 10) + first_digit

if(reversed_num == temp):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")