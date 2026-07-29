#11. Python Program to replace every blank space with hyphen in a string.

def replaceSpace(str):
    for i in str:
        if i == " ":
            str = str.replace(i, "-")
    return str

str = input("Enter a string : ")
print(replaceSpace(str))
 