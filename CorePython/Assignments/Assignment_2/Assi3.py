#convert distance given in feet and inches into meter  and centimeter

Feet = int(input("Enter the distance in feet: "))
Inch = int(input("Enter the distance in inches: "))

#perform operations

Meter = (Feet * 0.3048) + (Inch * 0.0254)
Centimeter = Meter * 100
#Display the result

print(f'The distance in meter is {Meter} and in centimeter is {Centimeter}')

