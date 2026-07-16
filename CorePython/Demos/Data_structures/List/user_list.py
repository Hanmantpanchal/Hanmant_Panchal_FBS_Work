def createList(li):
    n=int(input("how many elements you want to add :"))
    for i in range(n):
        ele = int(input("Enter the element :"))
        li.append(ele)

li = []
createList(li)
print(li)