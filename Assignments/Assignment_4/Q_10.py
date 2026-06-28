#10. WAP to check if given number is Perfect Number.

n = int(input("Enter a number : "))

i = 1

sum = 0

while i<n:
    if n%i==0:
        sum = sum+i
    i = i+1

if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")