#find the second largest element in the list 

def secondLargest(li):
    largest = li[0]
    second_largest = li[0]

    for i in li:
        if i > largest:
            second_largest = largest
            largest = i
           
        elif i > second_largest and i != largest:
            second_largest = i

    print("Largest =", largest)
    print("Second Largest =", second_largest)

li = [1, 2, 4, 5, 6, 7, 8]
secondLargest(li)