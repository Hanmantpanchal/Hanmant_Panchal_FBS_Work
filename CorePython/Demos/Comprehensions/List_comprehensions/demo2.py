#WAp to print square of each number 

#without comprehensions 
# number = [1 , 2 , 3 , 4 , 5]
# sqr = []

# for i in number:
#     sqr.append(i * i)
# print(sqr)


#Using comprehensions 

numbers = [1 , 2  , 3 , 4, 5, 6]
sqr = [i*i for i in numbers]
print(sqr)