#8. Python Program to Remove the Characters of Odd Index Values in a String

def remove_odd_index(s):
    new_string = ""

    for i in range(len(s)):
        if i % 2 == 0:      
            new_string = new_string + s[i]

    return new_string


s = input("Enter a string: ")
print(remove_odd_index(s))