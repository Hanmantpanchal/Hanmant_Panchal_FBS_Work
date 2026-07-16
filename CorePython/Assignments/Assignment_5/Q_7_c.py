#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.


n = int(input("Enter the number of terms: "))

sum = 0
term = 1

for i in range(1, n + 1):
    sum = sum + term
    term = term * 2

print("Sum =", sum)