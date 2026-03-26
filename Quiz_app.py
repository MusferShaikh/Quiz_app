import tkinter
import pyodbc
# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-U5D8MOU\\SQLEXPRESS;"
    "DATABASE=quiz_db;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

score = 0

# Fetch questions
cursor.execute("SELECT * FROM questions")
questions = cursor.fetchall()

for q in questions:
    print("\nQuestion:", q.question)
    print("1.", q.option1)
    print("2.", q.option2)
    print("3.", q.option3)
    print("4.", q.option4)
    
    answer = int(input("Enter your answer (1-4): "))
    
    if answer == q.correct_option:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n🎯 Final Score:", score, "/", len(questions))