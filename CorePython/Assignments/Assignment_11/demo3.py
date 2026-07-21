#3. Python Program to Sort the List According to the Second Element in Sublist
def secondSublist(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-i-1):
            if list1[j][1] > list1[j+1][1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

list1 = [[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]]
print(secondSublist(list1))


