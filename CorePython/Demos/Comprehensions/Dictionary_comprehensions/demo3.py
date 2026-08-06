#convert to uppercase

# names = ['raj' , 'amit' , 'rohan']

# result = {}

# for name in names :
#     result[name] = name.upper()
# print(result)


#comprehensions 

names = ['raj' , 'amit' , 'rohan']
result = {name : name.upper() for name in names}
print(result)

