#1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace(s):
    return s.replace("a","$")

s = input("Enter a string : ")
print(replace(s))
