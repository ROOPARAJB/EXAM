from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Connection
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="examregn"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_exam():
    data = request.form
    cursor = mysql_conn.cursor()
    try:
        # Inserting data into the database
        cursor.execute("INSERT INTO exams (student_name, register_number, register_course, exam_start, exam_end, comments) VALUES (%s, %s, %s, %s, %s, %s)",
                       (data['student_name'], data['register_number'], data['register_course'], data['exam_start'], data['exam_end'], data['comments']))
        mysql_conn.commit()
        cursor.close()
        return "Exam registered successfully"
    except Exception as e:
        return "Error: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
