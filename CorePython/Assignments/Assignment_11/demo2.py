#2. Python Program to Merge Two Lists and Sort it

def mergtwoList(list1 , list2):
    list3 = list1 + list2
    list3.sort()
    return list3
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(mergtwoList(list1,list2))



# def mergeTwoList(list1, list2):
#     list3 = list1 + list2

#     for i in range(len(list3)):
#         for j in range(len(list3) - 1 - i):
#             if list3[j] > list3[j + 1]:
#                 temp = list3[j]
#                 list3[j] = list3[j + 1]
#                 list3[j + 1] = temp

#     return list3


# list1 = [5, 2, 8]
# list2 = [1, 9, 3]

# print(mergeTwoList(list1, list2))
