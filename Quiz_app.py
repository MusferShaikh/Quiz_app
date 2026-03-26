import tkinter as tk
import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-U5D8MOU\\SQLEXPRESS;"
    "DATABASE=quiz_db;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# Fetch questions
cursor.execute("SELECT * FROM dbo.questions")
questions = cursor.fetchall()

# Variables
index = 0
score = 0

# Create window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("500x350")

# Question label
question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
question_label.pack(pady=20)

# Score label
score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack()

# Function to load question
def load_question():
    global index
    if index < len(questions):
        q = questions[index]
        question_label.config(text=q.question)

        btn1.config(text=q.option1, command=lambda: check_answer(1))
        btn2.config(text=q.option2, command=lambda: check_answer(2))
        btn3.config(text=q.option3, command=lambda: check_answer(3))
        btn4.config(text=q.option4, command=lambda: check_answer(4))
    else:
        question_label.config(text=f"Quiz Finished!\nFinal Score: {score}/{len(questions)}")
        btn1.pack_forget()
        btn2.pack_forget()
        btn3.pack_forget()
        btn4.pack_forget()

# Function to check answer
def check_answer(selected):
    global index, score
    if selected == questions[index].correct_option:
        score += 1
        score_label.config(text=f"Score: {score}")
    index += 1
    load_question()

# Buttons
btn1 = tk.Button(root, text="", width=30)
btn2 = tk.Button(root, text="", width=30)
btn3 = tk.Button(root, text="", width=30)
btn4 = tk.Button(root, text="", width=30)

btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)
btn4.pack(pady=5)

# Start quiz
load_question()

root.mainloop()