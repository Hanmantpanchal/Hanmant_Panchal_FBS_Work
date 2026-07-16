#e. x - x2/3 + x3/5 - x4/7 + …. to n terms

n = int(input("Enter the value of N: "))

sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum -= (i ** (i-2)) / (i-1)
    else:
        sum += (i ** (i-2)) / (i-1)

print("The sum of the series is:", sum)