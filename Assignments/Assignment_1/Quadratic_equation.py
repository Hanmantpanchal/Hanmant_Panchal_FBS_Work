#program to find the roots of quadratic equation

#take input from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

#perform operation 

d = (b**2) - (4*a*c)

r1= (-b + (d**0.5))/(2*a) # formula for finding roots ,rootvariable ** 0.5 is used to find square root
r2= (-b - (d**0.5))/(2*a)

#Display the roots

print(f"The roots of the quadratic equation are: {r1} and {r2}")