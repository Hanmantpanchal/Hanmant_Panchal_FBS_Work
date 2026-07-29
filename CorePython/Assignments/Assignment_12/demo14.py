#14 Python Program to count the occurrences of ach word in a string.

def countWordOccurrence(s):
    words = s.split()

    for i in words:
        count = words.count(i)
        print(i, ":", count)


s = input("Enter a string: ")
countWordOccurrence(s)