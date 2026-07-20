#10. Write a program to remove all occurrences of a given element in the list.

def remove_element(list1, element):
    new_list = []

    for i in list1:
        if i != element:
            new_list.append(i)

    return new_list


list1 = [1, 2, 3, 2, 4, 2, 5]
element = int(input("Enter element to remove: "))

print(remove_element(list1, element))