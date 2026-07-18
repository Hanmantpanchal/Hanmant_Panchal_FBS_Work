#Remove duplicate elements.

def removeDuplicate(li):

    for i in range(len(li)):
        duplicate = False

        for j in range(i):
            if li[i] == li[j]:
                duplicate = True
                break

        if duplicate == False:
            print(li[i], end=" ")


li = [1, 1, 2, 3, 5]

removeDuplicate(li)


        
        
