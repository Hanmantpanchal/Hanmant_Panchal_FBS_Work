#b. 1!+ 2! + 3! + 4!+..... + n!

def fact(n):
    fact = 1
    sum = 0 
    i = 1
    while i <= n:
        for j in range(1,i+1):
            fact = fact * j
        sum = sum + fact
        fact = 1
        i = i + 1
    return sum

num = int(input("Enter a number : "))
print("factorial sum is : ", fact(num))