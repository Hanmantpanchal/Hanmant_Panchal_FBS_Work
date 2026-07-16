# Binary searching
def binarySearching(li , ele):
    beg = 0 
    end = len(li)-1
    while(beg <= end+1):
        mid = (beg + end)//2
        if(ele == li[mid]):
            return mid
        elif(ele < li[mid]):
            end = mid-1
        elif(ele > li[mid]):
            beg = mid+1

    else:
        return -1 

li = [10 , 20 , 30 , 40 , 50 , 60 , 70]

element = int(input("Enter the element "))
res = binarySearching(li , element)

if res != -1 :
    print("element prest at" , res)
else:
    print("element not present ")