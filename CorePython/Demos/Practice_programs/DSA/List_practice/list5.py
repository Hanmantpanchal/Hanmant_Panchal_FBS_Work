#1. Python Program to Put Even and Odd elements of a List into two Different Lists

def evenOdd(li):
    even = []
    odd = []   
    for i in li:
        
        if i % 2 == 0:
            even.append(i)
        
        else:
            odd.append(i)

    print(even)
    print(odd)

li = [1, 2, 3 ,4 , 5 , 6, 7, 8, 9]

evenOdd(li)

