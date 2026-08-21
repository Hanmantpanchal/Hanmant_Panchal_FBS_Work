import tkinter as tk

window = tk.Tk()

window.title("Greeting App")
window.geometry("400x300")


def show_name():
    name = entry.get()
    label.config(text="Hello " + name)


label = tk.Label(window, text="Enter your name")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(
    window,
    text="Submit",
    command=show_name
)
button.pack()

window.mainloop()