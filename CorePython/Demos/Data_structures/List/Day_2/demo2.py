#find the largest and smallest element 

def largestSmallest(li):
    largest = li[0]
    smallest = li[0]

    for i in li:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i
    print("largest",largest)
    print("smallest",smallest)
li = [45 , 70 , 18 , 20 , 21 ]
largestSmallest(li)  

        

