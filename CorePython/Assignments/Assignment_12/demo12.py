#12. Python Program to count number of lowercase characters in a string.

def lowercase_count(str):
    count = 0
    for i in str:
        if i.islower():
            count += 1
    return count

str = input("Enter a string: ")
print("Number of lowercase characters in the string is:", lowercase_count(str))
