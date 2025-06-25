import flask
from flask import request, jsonify
import student_generator_v2 as sg

# Create a flask app object
app = flask.Flask(__name__)
# App refers to a flask object.  Flask is a server that users can connecto to and ask for information

# Tell the server to reload each time the code changes
app.config["DEBUG"] = True

# Create a route to display our name
# this line, when going to the website, tells the program to run the function below it using the GET method
@app.route('/', methods = ['GET'])
def index():
    return "<h1> My name is Steven Shaw </h1>"

# Create a route to return all student data
# 127.0.0.1:5000/api/students/all
@app.route('/api/students/all', methods = ['GET'])
def api_all():
    # Load student dictionaries 
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

# Create a route to return students by major
@app.route('/api/majors/<string:major>', methods = ['GET'])
# <string:major> passes major as an input for the function
def api_students_by_major(major:str):
    print(major)
    # Get students with that major
    student_dictionaries = sg.get_student_dictionaries()
    major_students = []
    for student in student_dictionaries:
        if student["major"].lower() == major.lower():
            major_students.append(student)

    return jsonify(major_students)

# Run application
app.run()
