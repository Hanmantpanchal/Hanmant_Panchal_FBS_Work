#a. 1! + 2! + 3! + 4! + .....n!

n = int(input("Enter a number : "))
fact = 1 
sum = 0

for i in range(1,n+1):
    while i>0:
        fact = fact*i
        i = i-1# decrementing the value of i
    sum = sum + fact
    fact = 1 # resetting the fact variable to 1 for the next iteration
print(sum)

    