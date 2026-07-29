#13. Python Program to count number of digits and letters in a string.

def countDigitLetter(s):
    letters = 0
    digits = 0

    for i in s:
        if i.isalpha():
            letters = letters + 1
        elif i.isdigit():
            digits = digits + 1

    print("Letters :", letters)
    print("Digits  :", digits)


s = input("Enter a string: ")
countDigitLetter(s)
