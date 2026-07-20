#8. Write a program to create a duplicate of an existing list. It should not point to same list.


def duplicate(list1):
    return list1.copy()

list1 = [1,2,3,4,5,6,7,8,9,10]

result = duplicate(list1)

print(result)


# def duplicate(list1):
#     list2 = []

#     for i in list1:
#         list2.append(i)

#     return list2

# list1 = [1,2,3,4,5]
# print(duplicate(list1))
