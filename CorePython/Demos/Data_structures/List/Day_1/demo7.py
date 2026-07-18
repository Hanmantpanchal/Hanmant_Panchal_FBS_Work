#print the sum of all element 

def sumElement(li):
    sum = 0 
    for i in li:
        sum = sum + i
    return sum
li = [2 , 4 , 6, 7, 4, 7]
res = sumElement(li)

print(res)