#10. Write a program to check if entered year is a leap year or not.
def year_check(year):

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")
    return year

yr = int(input("Enter the year: "))
print(year_check(yr))