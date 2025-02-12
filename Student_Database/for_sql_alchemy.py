from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy with MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/bala'  # Replace with your MySQL URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object
db = SQLAlchemy(app)

# Define the Student model (equivalent to the students table)
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'

# Home Page with Student Form
@app.route('/')
def index():
    return render_template('student_form.html')

# Route to Submit Student Form
@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        course = request.form['course']
        location = request.form['location']

        try:
            # Create a new student instance
            new_student = Students(name=name, age=age, gender=gender, course=course, location=location)

            # Add the student to the session and commit to the database
            db.session.add(new_student)
            db.session.commit()

            return redirect('/students')  # Redirect to student list after adding
        except Exception as e:
            return f"An error occurred: {e}"

# Route to List All Students
@app.route('/students')
def list_students():
    try:
        # Retrieve all students from the database
        students = Students.query.all()

        return render_template('students_list.html', students=students)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=False)
