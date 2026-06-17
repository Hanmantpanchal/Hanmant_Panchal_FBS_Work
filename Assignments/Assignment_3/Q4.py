#4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))

if ((a + b > c) and (a + c > b) and (b + c > a)):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")