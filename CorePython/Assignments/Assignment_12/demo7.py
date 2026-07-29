#7. Python Program to Calculate the Length of a String Without Using a Library Function 

def string_len(string):
    count = 0
    for i in string:
        count += 1
    return count

string = input("Enter a string: ")
print("Length of the string is: ",string_len(string))
