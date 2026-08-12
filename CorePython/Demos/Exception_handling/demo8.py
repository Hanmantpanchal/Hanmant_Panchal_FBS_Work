try:
    balance = 10000
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance")

    print("Withdrawal successful")
    print("Remaining balance:", balance - amount)

except ValueError as e:
    print("Error:", e)

finally:
    print("Thank you for using ATM")