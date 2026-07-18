#find the third smallest number
# Find the third smallest element in the list

def thirdSmall(li):
    smallest = li[0]
    second_small = li[0]
    third_small = li[0]

    for i in li:
        if i < smallest:
            third_small = second_small
            second_small = smallest
            smallest = i

        elif i < second_small and i != smallest:
            third_small = second_small
            second_small = i

        elif i < third_small and i != second_small and i != smallest:
            third_small = i

    print(third_small)


li = [44, 42, 18, 17, 46, 21]

thirdSmall(li)

