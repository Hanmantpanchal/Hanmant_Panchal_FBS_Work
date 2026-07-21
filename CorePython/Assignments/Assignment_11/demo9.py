#9. Write a program to create three lists of numbers, their squares and cubes

def square_cubes():
    for i in range(1,11):
        list1.append(i)
        list2.append(i*i)
        list3.append(i*i*i)
    return list1,list2,list3

list1=[]
list2=[]
list3=[]

list1,list2,list3=square_cubes()
print("List1:",list1)
print("List2:",list2)
print("List3:",list3)
