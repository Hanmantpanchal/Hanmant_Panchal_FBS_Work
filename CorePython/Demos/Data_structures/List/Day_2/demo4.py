#Search an element in a list (Linear Search).

def linearSearch(li , searchEle):
    for i in range(len(li)):
        if li[i]==searchEle:
            return i
    else:
        return -1
    
n = int(input("Enter the element you want to search"))

li = [1 , 2 , 3  , 4 , 6]

res = linearSearch(li , n)

if res != -1 :
    print(f"element {n} present at index :{res}")
else:
    print("element not present in the list ")
        