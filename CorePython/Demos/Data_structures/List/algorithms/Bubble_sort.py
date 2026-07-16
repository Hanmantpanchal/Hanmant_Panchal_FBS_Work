#WAP to print bubble sort

def bubble_sort(list1): 
    size = len(list1) 
    for i in range(1 , size): 
        for j in range(0, size-i-1):
            if list1[j] > list1[j+1] : 
                list1[j], list1[j+1] = list1[j+1], list1[j]

list1 = [5, 1, 4, 2, 8]
bubble_sort(list1)
print ("Sorted array is:", list1)
