#write a program to print prime numbr in given range 

a = 2
b= 10

for i in range(a,b+1):
    flag = 0
    for j in range(2,i):
        if i%j==0:
            flag = 1
            break
    if flag == 0:
        print(i)