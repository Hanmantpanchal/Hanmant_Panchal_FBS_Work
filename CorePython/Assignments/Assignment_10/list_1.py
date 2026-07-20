#1. Write a program to find sum of all elements of list

def sum_list(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum
list1 = [1,2,3,4,5,6,7,8,9,10]
print(sum_list(list1))


