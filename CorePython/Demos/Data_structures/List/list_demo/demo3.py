#smallest element in list

def smallest_element(list1):
    smallest = list1[0]
    for i in list1:
        if i < smallest:
            smallest = i
    return smallest

list1 = [10 , 18 , 27 , 40 , 5 , 6 , 7 , 8 , 9 , 10]
print(smallest_element(list1))