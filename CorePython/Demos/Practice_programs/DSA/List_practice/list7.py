#3. Python Program to Sort the List According to the Second Element in Sublist

li = [[1 , 5] , [3 , 2] , [4 , 8] , [2 , 1] , [5 , 6]]

# for i in li:
#     for j in i:
#         print(j)



li = [
    [1, 5],
    [3, 2],
    [4, 8],
    [2, 1],
    [5, 6]
]

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i][1] > li[j][1]:
            li[i], li[j] = li[j], li[i]

print("Sorted List:")
print(li)
    


    
