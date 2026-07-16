#insertion sort
def insertionSort(li):
    size = len(li)
    for i in range(1 , size):
        key = li[i]
        j = i-1
        while j>=0 and key < li[j]:
            li[j+1] = li[j]
            j = j-1
        li[j+1] = key
li = [40 , 30 , 20 , 10]
insertionSort(li)
print("sorted list is :" , li)