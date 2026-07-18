#find the third largest element in the list

# Find the third largest element in the list

def thirdLargest(li):
    largest = li[0]
    second_largest = li[0]
    third_largest = li[0]

    for i in li:
        if i > largest:
            third_largest = second_largest
            second_largest = largest
            largest = i

        elif i > second_largest and i != largest:
            third_largest = second_largest
            second_largest = i

        elif i > third_largest and i != second_largest and i != largest:
            third_largest = i

    print("Largest =", largest)
    print("Second Largest =", second_largest)
    print("Third Largest =", third_largest)


li = [1, 2, 3, 4, 5]
thirdLargest(li)

