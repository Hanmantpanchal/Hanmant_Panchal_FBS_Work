# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.


def check_element(list1, num):
    count = 0

    for i in list1:
        if i == num:
            count += 1

    if count > 0:
        print(num, "is present in the list")
        print("It is present", count, "times")
    else:
        print(num, "is not present in the list")


list1 = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter the number: "))

check_element(list1, num)



# def checkElement(list1, num):
#     count = 0

#     for i in list1:
#         if i == num:
#             count += 1

#     return count


# list1 = [10, 20, 30, 20, 40, 20, 50]

# num = int(input("Enter number: "))

# result = checkElement(list1, num)

# if result > 0:
#     print("Element is present")
#     print("Count =", result)
# else:
#     print("Element is not present")




#using built in function

# def checkElement(list1, num):
#     if num in list1:
#         print("Element is present")
#         print("Count =", list1.count(num))
#     else:
#         print("Element is not present")


# list1 = [10, 20, 30, 20, 40, 20, 50]

# num = int(input("Enter number: "))

# checkElement(list1, num)