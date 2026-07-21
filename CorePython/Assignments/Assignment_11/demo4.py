#4. Python Program to Find the Second Largest Number in a List Using Bubble Sort

def second_largest(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list[-2]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Second largest number in the list is:", second_largest(list))
