#double each number using map 

number = [1 ,2 , 3 , 4]

result = list(map(lambda x : x*2 , number))

print(result)


# with multiple paramtere 

def add(n1 , n2):
    return n1 + n2 
data = [1,2,3,4,5,6,7,8,9,10]
data1 = [1,2,3,4,5,6,7,8,9,10]

res = list(map(add , data , data1))
print(res)