#Python Program to Find the Union of two Lists

def unionList(list1, list2):
    result = []

    for i in list1:
        if i not in result:
            result.append(i)

    for i in list2:
        if i not in result:
            result.append(i)

    return result


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(unionList(list1, list2))