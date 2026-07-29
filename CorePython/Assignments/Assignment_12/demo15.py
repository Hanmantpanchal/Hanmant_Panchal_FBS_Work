#15. Python Program to find larger string without using built-in functions.

def largerString(str1, str2):
    count1 = 0
    count2 = 0

    for i in str1:
        count1 = count1 + 1

    for i in str2:
        count2 = count2 + 1

    if count1 > count2:
        print("Larger String :", str1)
    elif count2 > count1:
        print("Larger String :", str2)
    else:
        print("Both strings are equal in length")


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

largerString(str1, str2)