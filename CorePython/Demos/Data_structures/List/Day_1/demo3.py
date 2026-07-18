#find the length of  list without using len() function 


def findLength(li):
    count = 0 
    
    for i in li :
        count = count + 1
    return count 
li = [1,2,3,4,5]

res = findLength(li)

print(res)
