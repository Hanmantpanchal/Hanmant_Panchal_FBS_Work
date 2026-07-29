#6. Python Program to Take in a String and Replace Every Blank Space with Hyphen

def replace_space(string):
    return string.replace(" ","-")

string = input("Enter a string : ")

print(replace_space(string))
