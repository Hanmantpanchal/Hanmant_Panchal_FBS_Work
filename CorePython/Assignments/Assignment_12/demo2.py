#2. Python Program to Remove the nth Index Character from a Non-Empty String

def remove_char(s,n):
    return s[:n] + s[n+1:]

s = input("Enter a string : ")
n = int(input("Enter a index : "))

print(remove_char(s,n))
