#1. Python Program to Put Even and Odd elements of a List into two Different Lists

def even_odd(list1):
    even_list = []
    odd_list = []
    for i in list1:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print("Even List : ",even_list)
    print("Odd List : ",odd_list)


list1 = [1,2,3,4,5,6,7,8,9,10]
even_odd(list1)
