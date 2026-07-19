#2. Write a program to calculate area of circle
def areaofcircle(radius):
    #function body , return statement
    return 3.14*radius*radius

r = int(input("Enter the radius of circle : "))

Area = areaofcircle(r)

print("Area of circle is : ",Area)
