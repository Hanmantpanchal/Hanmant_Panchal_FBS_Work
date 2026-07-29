#10. Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions 

def largestString(str1 , str2):
    count = 0
    count1 = 0
    for i in str1:
        count += 1
    for i in str2:
        count1 += 1
    if count > count1:
        print(str1)
    else:
        print(str2)

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
largestString(str1 , str2)
