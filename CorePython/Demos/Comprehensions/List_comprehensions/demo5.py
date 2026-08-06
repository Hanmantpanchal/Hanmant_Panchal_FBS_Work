#WAP to print nested loop

# pairs = []

# for i in range(1 , 4):
#     for j in range(1 , 3):
#         pairs.append((i , j))
# print(pairs)



#using comprehensions

pairs = [(i , j) for i in range(1 , 4)  for j in range(1 , 8)]
print(pairs)