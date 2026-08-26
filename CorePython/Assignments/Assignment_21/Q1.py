# Python Assignment - (Exception Handling)
# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.

class InvalidNumberError(Exception):
    pass


class InvalidOperatorError(Exception):
    pass


try:

    # Take numbers from user
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Convert to float
    try:
        num1 = float(num1)
        num2 = float(num2)

    except ValueError:
        raise InvalidNumberError("Please enter valid numbers.")

    # Take operator
    operator = input("Enter operator (+, -, *, /): ")

    # Check operator
    if operator not in ["+", "-", "*", "/"]:
        raise InvalidOperatorError("Invalid operator. Use +, -, *, or /.")

    # Perform operation
    if operator == "+":

        result = num1 + num2

    elif operator == "-":

        result = num1 - num2

    elif operator == "*":

        result = num1 * num2

    elif operator == "/":

        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        result = num1 / num2

    print("Result:", result)


except InvalidNumberError as e:
    print("Error:", e)

except InvalidOperatorError as e:
    print("Error:", e)

except ZeroDivisionError as e:
    print("Error:", e)