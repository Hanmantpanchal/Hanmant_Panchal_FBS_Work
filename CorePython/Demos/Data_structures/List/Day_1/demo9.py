#find the maxinun element without using max

def maxElement(li):
    max_ele = li[0]

    for i in li:
        if i > max_ele:
            max_ele = i
    return max_ele

li = [45 , 567 , 667 , 34 , 678 ]

res = maxElement(li)

print(res)