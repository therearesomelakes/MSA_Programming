import flask
from flask import request, jsonify
import student_generator_v2 as sg

# Create a flask app object
app = flask.Flask(__name__)
# App refers to a flask object.  Flask is a server that users can connecto to and ask for information

# Tell the server to reload each time the code changes
app.config["DEBUG"] = True

'''
Function to query the student dictionaries based on a search key
Input: search key
Output: list of results
'''
def search_student_data(search_key, search_value):
    student_dictionaries = sg.get_student_dictionaries()
    list_of_results = []
    # Searches student dictionaries for a key that matches the value
        # Ex: matching majors until one finds a major that is "ecology"
    for student in student_dictionaries:
        if student[search_value].lower() == search_key.lower():
            list_of_results.append(student)
    return list_of_results

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
    major_students = search_student_data(major, "major")

    return jsonify(major_students)

# Create a route to return a student based on an id url
@app.route('/api/students/<string:id>', methods = ['GET'])
def api_student_by_id(id:str):
    returned_student = search_student_data(id, "id")
    return jsonify(returned_student)

# Can't do /api/students/<string:class_rank>, because that would create a conflict with /api/students/<string:id>
@app.route('/api/students/class/<string:class_rank>', methods = ['GET'])
def api_student_by_class(class_rank:str):
    student_by_class = search_student_data(class_rank, "class")
    return jsonify(student_by_class)

# Run application
app.run()
