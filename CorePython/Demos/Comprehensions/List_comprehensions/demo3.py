#WAP to print find even number and print it 

# even = []

# for i in range(1 , 11):
#     if i % 2 == 0:
#         even.append(i)
# print(even)



#using comprehensions 

even = [i for i in range(1 , 11) if i % 2 == 0]

print(even)