#2. Write a program to find maximum and minimum element in a list.
def max_min(list1):
    max1 = list1[0]
    min1 = list1[0]
    for i in list1:
        if i > max1:
            max1 = i
        if i < min1:
            min1 = i
    print("Maximum element is : ", max1)
    print("Minimum element is : ", min1)
list1 = [1,2,3,4,5,6,7,8,9,10]
max_min(list1)
