#9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String

def countWordCharacter(s):
    words = 1
    characters = 0

    for i in s:
        if i == " ":
            words = words + 1
        else:
            characters = characters + 1

    print("Number of Words :", words)
    print("Number of Characters :", characters)


s = input("Enter a string: ")
countWordCharacter(s)