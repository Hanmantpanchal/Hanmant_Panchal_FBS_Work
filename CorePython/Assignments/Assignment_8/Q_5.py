#5. Sum of all prime numbers between 1 to n

def printPrime(n):
    sum = 0 
    for i in range(2, n + 1):
        count = 0
        

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 2:
            sum = sum + i
    return sum

num = int(input("Enter the number: "))
print("Sum of all prime numbers between 1 to n is : " , printPrime(num))