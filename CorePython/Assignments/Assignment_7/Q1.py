for i in range(1 ,6):
    for j in range(1 , 6-i):
        print(" ", end=" ")
    for j in range(1 , 2*i):
        if j == 1 or j == 2 * i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
   
for i in range(1,5):
    for j in range(1 ,i+1):
        print(" " , end=" ")
    for j in range( 1  , (5-i)*2 ):
        if j == 1 or j == 2 *(5-i) - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
