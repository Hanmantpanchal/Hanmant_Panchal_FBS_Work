# 4. Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
# questions one at a time and allow the user to select an answer. Provide feedback on
# whether the selected answer is correct or incorrect.

from tkinter import *
from tkinter import messagebox


# Questions
questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": ["Java", "Python", "C++", "PHP"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is used to store multiple values?",
        "options": ["int", "float", "list", "bool"],
        "answer": "list"
    },
    {
        "question": "Which library is used to create GUI applications in Python?",
        "options": ["NumPy", "Pandas", "Tkinter", "Matplotlib"],
        "answer": "Tkinter"
    }
]


current_question = 0
score = 0


def show_question():
    question_label.config(
        text=questions[current_question]["question"]
    )

    option1.config(text=questions[current_question]["options"][0])
    option2.config(text=questions[current_question]["options"][1])
    option3.config(text=questions[current_question]["options"][2])
    option4.config(text=questions[current_question]["options"][3])

    selected_answer.set("")


def check_answer():
    global current_question
    global score

    selected = selected_answer.get()

    if selected == "":
        messagebox.showwarning(
            "Warning",
            "Please select an answer."
        )
        return

    correct_answer = questions[current_question]["answer"]

    if selected == correct_answer:
        score += 1
        messagebox.showinfo(
            "Result",
            "Correct Answer!"
        )
    else:
        messagebox.showerror(
            "Result",
            "Incorrect Answer!\nCorrect Answer: " + correct_answer
        )

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo(
            "Quiz Completed",
            "Your Score: " + str(score) +
            "/" + str(len(questions))
        )

        root.destroy()


# Create window
root = Tk()

root.title("Quiz Game")
root.geometry("600x450")


# Heading
Label(
    root,
    text="Python Quiz Game",
    font=("Arial", 22, "bold")
).pack(pady=20)


# Question
question_label = Label(
    root,
    text="",
    font=("Arial", 15),
    wraplength=500
)

question_label.pack(pady=20)


# Store selected answer
selected_answer = StringVar()


# Options
option1 = Radiobutton(
    root,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 13)
)
option1.pack(anchor="w", padx=100, pady=5)


option2 = Radiobutton(
    root,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 13)
)
option2.pack(anchor="w", padx=100, pady=5)


option3 = Radiobutton(
    root,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 13)
)
option3.pack(anchor="w", padx=100, pady=5)


option4 = Radiobutton(
    root,
    text="",
    variable=selected_answer,
    value="",
    font=("Arial", 13)
)
option4.pack(anchor="w", padx=100, pady=5)


# Submit button
Button(
    root,
    text="Submit Answer",
    command=check_answer,
    font=("Arial", 12)
).pack(pady=25)


# Display first question
show_question()


# Run application
root.mainloop()