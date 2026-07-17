#

for i in range(1 , 6):
    for j in range(1 , 6-i):
        print(" " , end=" ")
    
    for j in range(1 , i+1):
        print(j, end=" ")

    n = i-1
    
    for j in range(i-1):
        print(n, end=" ")
        n = n-1
        
    print()