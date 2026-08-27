# 2. Build a currency converter application that converts between different currencies. The
# user should be able to enter an amount, select the input currency, select the output
# currency, and see the converted amount.

from tkinter import *
from tkinter import messagebox


# Currency conversion rates with respect to INR
rates = {
    "INR": 1,
    "USD": 95.35,
    "EUR": 110,
    "GBP": 127,
    "JPY": 0.65
}


def convert():
    try:
        amount = float(entry_amount.get())

        from_currency = from_var.get()
        to_currency = to_var.get()

        # Convert source currency to INR
        inr_amount = amount * rates[from_currency]

        # Convert INR to target currency
        result = inr_amount / rates[to_currency]

        result_label.config(
            text=f"{amount} {from_currency} = {result:.2f} {to_currency}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")


# Create window
root = Tk()

root.title("Currency Converter")
root.geometry("450x350")


# Heading
Label(
    root,
    text="Currency Converter",
    font=("Arial", 20, "bold")
).pack(pady=20)


# Amount
Label(root, text="Enter Amount").pack()

entry_amount = Entry(root)
entry_amount.pack(pady=5)


# From Currency
Label(root, text="From Currency").pack(pady=5)

from_var = StringVar()
from_var.set("INR")

from_menu = OptionMenu(
    root,
    from_var,
    "INR",
    "USD",
    "EUR",
    "GBP",
    "JPY"
)

from_menu.pack()


# To Currency
Label(root, text="To Currency").pack(pady=5)

to_var = StringVar()
to_var.set("USD")

to_menu = OptionMenu(
    root,
    to_var,
    "INR",
    "USD",
    "EUR",
    "GBP",
    "JPY"
)

to_menu.pack()


# Convert Button
Button(
    root,
    text="Convert",
    command=convert
).pack(pady=20)


# Result
result_label = Label(
    root,
    text="Result will appear here",
    font=("Arial", 14, "bold")
)

result_label.pack(pady=10)


# Run application
root.mainloop()