#4. Write a program to reverse the list.
def reverse_list(list1):
    rev = []

    for i in range(len(list1) - 1, -1, -1):
        rev.append(list1[i])

    return rev

list1 = [1,2,3,4,5,6,7,8,9,10]
print(reverse_list(list1))


# def reverse_list(list1):
#     rev = []

#     for i in list1:
#         rev.insert(0, i)

#     return rev


# list1 = [1, 2, 3, 4, 5]
# print(reverse_list(list1))
