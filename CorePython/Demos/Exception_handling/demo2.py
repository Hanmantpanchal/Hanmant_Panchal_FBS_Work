try:
    num = int(input("Enter number: "))
    print(100 / num)

except ZeroDivisionError:
    print("Number cannot be zero")

except ValueError:
    print("Please enter a valid number")