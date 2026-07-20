#13 . Write a program to print list after removing even numbers.

def remove_even(list1):
    for i in list1:
        if i % 2 == 0:
            list1.remove(i)
    return list1

list1 = [1,2,3,4,5,6,7,8,9,10]
print(remove_even(list1))
