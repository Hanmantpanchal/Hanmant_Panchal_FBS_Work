# 1 2 3 4 5 6
# 6 5 4 3 2 1
# 1 2 3 4 5 6
# 6 5 4 3 2 1
# 1 2 3 4 5 6
# 6 5 4 3 2 1

for i in range(1 , 7):
    if i % 2==0:
        for j in range(6 , 0 , -1):
            print(j  , end=" ")
        print()
    else:
        for j in range(1 , 7):
            print(j , end=" ")
        print()
