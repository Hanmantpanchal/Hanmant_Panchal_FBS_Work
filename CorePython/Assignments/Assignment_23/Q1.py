# 1. Develop a simple login system with a username and password field. Implement user
# authentication, and show a success message if the login is successful, or an error
# message if the login fails.

from tkinter import *
from tkinter import messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password!")


# Create window
root = Tk()

root.title("Login System")
root.geometry("400x300")


# Username
Label(root, text="Username").pack(pady=10)

entry_username = Entry(root)
entry_username.pack()


# Password
Label(root, text="Password").pack(pady=10)

entry_password = Entry(root, show="*")
entry_password.pack()


# Login Button
Button(root, text="Login", command=login).pack(pady=20)


# Run application
root.mainloop()