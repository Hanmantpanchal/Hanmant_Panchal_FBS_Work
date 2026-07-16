#6. Write a program to print first n prime numbers.

n=int(input("Enter a number : "))

i = 2

count = 0

while i <= n:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        print(i)
        count += 1
    i += 1

print("Total prime numbers :", count)