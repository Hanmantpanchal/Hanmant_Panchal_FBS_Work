# 3. Design a basic calculator to perform +,-,/,*

from tkinter import *
from tkinter import messagebox


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return

            result = num1 / num2

        result_label.config(text="Result = " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


# Create window
root = Tk()

root.title("Basic Calculator")
root.geometry("400x350")


# Heading
Label(
    root,
    text="Basic Calculator",
    font=("Arial", 20, "bold")
).pack(pady=20)


# First number
Label(root, text="Enter First Number").pack()

entry1 = Entry(root)
entry1.pack(pady=5)


# Second number
Label(root, text="Enter Second Number").pack()

entry2 = Entry(root)
entry2.pack(pady=5)


# Operation
Label(root, text="Select Operation").pack(pady=5)

operation_var = StringVar()
operation_var.set("+")

operation_menu = OptionMenu(
    root,
    operation_var,
    "+",
    "-",
    "*",
    "/"
)

operation_menu.pack()


# Calculate button
Button(
    root,
    text="Calculate",
    command=calculate
).pack(pady=20)


# Result
result_label = Label(
    root,
    text="Result = ",
    font=("Arial", 14, "bold")
)

result_label.pack(pady=10)


# Run application
root.mainloop()