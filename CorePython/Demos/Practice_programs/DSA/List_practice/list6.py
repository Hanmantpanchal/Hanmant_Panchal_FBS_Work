# 2. Python Program to Merge Two Lists and Sort it

def mergesort(li1 , li2):
    li3 = li1 + li2
    for i in range(len(li3)):
        for j in range(len(li3)-1):
            if li3[j] > li3[j+1]:
                li3[j], li3[j+1] = li3[j+1], li3[j]
    return li3

li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(mergesort(li1, li2))


