from flask import Flask, render_template, request, redirect
import pyodbc

app = Flask(__name__)

# DB Connection
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-U5D8MOU\\SQLEXPRESS;"
    "DATABASE=quiz_db;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

score = 0
index = 0

# Load questions
cursor.execute("SELECT * FROM dbo.questions")
questions = cursor.fetchall()

@app.route('/', methods=['GET', 'POST'])
def quiz():
    global index, score

    if request.method == 'POST':
        selected = int(request.form.get('option'))
        if selected == questions[index].correct_option:
            score += 1
        index += 1

    if index < len(questions):
        q = questions[index]
        return render_template('quiz.html', q=q, index=index)
    else:
        final_score = score
        index = 0
        score = 0
        return render_template('result.html', score=final_score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)