#find largest element in list

def largest_element(list1):
    max = list1[0]
    for i in list1:
        if i > max:
            max = i
    return max

list1 = [1,2,3,4,5,6,7,8,9,10]
print(largest_element(list1))
