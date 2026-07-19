#1. Write a program to calculate area of rectangle using function 

#function defination
def areaofRectangle(Length , Width):

    # function body , return statement
    return Length * Width

#user input
L = int(input("Enter the length of rectangle : "))
W = int(input("Enter the width of rectangle : "))

#function call
Area = areaofRectangle(L , W)

#print the result
print("Area of rectangle is : ",Area)
