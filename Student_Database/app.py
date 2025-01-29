from flask import Flask, render_template, request, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'root'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'bala'

mysql = MySQL(app)

# Home Page with Student Form
@app.route('/')
def index():
    return render_template('student_form.html')

# Route to Submit Student Form
@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':

        #request.get_json()
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        course = request.form['course']
        location = request.form['location']

        try:
            cur = mysql.connection.cursor()
            query = "INSERT INTO students (name, age, gender, course, location) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, (name, age, gender, course, location))
            mysql.connection.commit()
            cur.close()
            return redirect('/students') # Redirect to student list after adding
        except Exception as e:

            return f"User Already available"

# Route to List All Students
@app.route('/students')
def list_students():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students")
        students = cur.fetchall()
        cur.close()



        return render_template('students_list.html', students=students)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=False)
