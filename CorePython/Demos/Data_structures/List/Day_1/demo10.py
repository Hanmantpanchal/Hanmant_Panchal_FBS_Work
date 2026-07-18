#find the minimum element wihtout using min()

def minElement(li):
    smallest = li[0]

    for i in li:
        if i < smallest:
            smallest = i

    return smallest


li = [4, 67, 4, 45, 57]

res = minElement(li)

print(res)