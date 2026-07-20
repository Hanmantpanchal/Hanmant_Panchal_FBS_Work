#9.9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

def even_odd(list1):
    even_list = []
    odd_list = []

    for i in list1:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print("Even List:", even_list)
    print("Odd List:", odd_list)


n = int(input("Enter number of elements: "))

list1 = []

for i in range(n):
    num = int(input("Enter element: "))
    list1.append(num)

even_odd(list1)
