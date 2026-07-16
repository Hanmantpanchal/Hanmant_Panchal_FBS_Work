#WAP to print all integers upto nth that arent divisible by 2 and 3 

n = int(input("Enter a number : "))
i =1 
while(i<n):
    if(i%2!=0 and i%3!=0):
        print(i)
    i+=1