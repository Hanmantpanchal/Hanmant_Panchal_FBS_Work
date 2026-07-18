#print frequency of an element 

def frequency(li , ele):
    print(li.count(ele))

li = [1 , 2 , 2, 2, 3 , 4 , 5 , 6 ]

element = int(input("Enter the element :"))

frequency(li , element)



#normal way ------

def freq(li , ele):
    search = 0 
    for i in li :
        if i == ele:
            search = search + 1
    return search

li = [1 , 2 , 2, 2, 3 , 4 , 5 , 6 ]
ele = int(input("Enter the element :"))

res = freq(li , ele)

print(res)

