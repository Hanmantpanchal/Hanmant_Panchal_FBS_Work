# a = 10
# b = 0

# print(a / b)
# print("Program End")

#ZeroDivisionError: division by zero



try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

