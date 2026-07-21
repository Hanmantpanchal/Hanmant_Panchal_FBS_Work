#7. Python Program to Find the Intersection of Two Lists

def intersection(list1,list2):
    list3=[]
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

list1=[1,2,3,4,5,6,7,8,9]
list2=[4,5,6,7,8,9,10,11,12]
print(intersection(list1,list2))


