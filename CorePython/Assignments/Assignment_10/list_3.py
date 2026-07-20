#3. Write a program to find the second largest element in the list.without built in function
def secondLargest(li):
    largest = li[0]
    second = li[0]

    for i in li:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i

    return second

li = [12, 45, 6, 78, 23, 67]

result = secondLargest(li)
print("Second Largest =", result)
    
