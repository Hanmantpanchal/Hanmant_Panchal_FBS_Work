#WAP to print all odd number until n 

n = int(input("enter the number :"))

i = 1

while(n>i):
    print(i)
    i+=2




#using for loop 

no = int(input("enter the number :"))

for i in range(1 , n):
    if(i%2 != 0 ):
        print(i)
        