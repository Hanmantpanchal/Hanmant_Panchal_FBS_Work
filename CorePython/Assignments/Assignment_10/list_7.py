#7. Write a program to create a new list from existing list which contains cube of each number of list.

def cubeofList(list1):
    list2 = []
    for i in list1:
        list2.append(i**3)
    return list2

list1 = [1,2,3,4,5,6,7,8,9,10]
result = cubeofList(list1)
print(result)
