def factofNumber(n):
    if n==0:
        return 1
    else:
        return n*factofNumber(n-1)

n=int(input("Enter a number: "))
print("Factorial of",n,"is",factofNumber(n))
