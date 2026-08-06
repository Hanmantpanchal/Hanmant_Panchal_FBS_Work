# 50 even number only

# even = {}

# for i in range(1 , 11):
#     if i % 2 == 0:
#         even[i] = i*i
# print(even)

#comprehensions 

even = {i : i*i for i in range(1 , 11) if i % 2 == 0}
print(even)