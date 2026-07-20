#6. Write a program to remove duplicates from the list.

def removeDuplicate(list1):
    newList = []

    for i in list1:
        if i not in newList:
            newList.append(i)

    return newList


list1 = [10, 20, 30, 20, 40, 10, 50, 30]

result = removeDuplicate(list1)

print(result)
