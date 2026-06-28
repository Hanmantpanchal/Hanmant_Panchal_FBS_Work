#9. WAP to print all numbers in a range divisible by a given number.

n = int(input("Enter a range : "))
Divisible = int(input("Enter a number : "))

i =1
while i<=n:
    if i%Divisible==0:
        print(i)
    i=i+1

