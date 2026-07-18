#find the avearage of list element 

def averageList(li):
    count = 0
    sum = 0 
    for i in range(len(li)):
        count = count + 1
        sum = sum + li[i]
    avg = sum / count     
    return avg

li = [1 , 2 , 3 , 4 , 5]

res = averageList(li)

print(res)