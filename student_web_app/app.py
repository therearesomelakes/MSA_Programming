from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

# Make a Flask app
app = Flask(__name__)
app.config["DEBUG"] = True

# Set secret key
app.config["SECRET_KEY"] = "meow_secret_key_:3"


'''
Function to request student data from the api
Input: url
Output: json student data
'''
def get_student_data(url:str):
    # Make a request
    response = requests.get(url)

    # Convert response object to json
    response_json = response.json()
    return response_json

# Create a route for the website index.  Will display all student data
@app.route('/', methods = ['GET'])
def index():
    # Make a request to the student api
    url = 'http://127.0.0.1:5000/api/students/all'

    # Get the student data
    student_data = get_student_data(url)
    return render_template('index.html', student_data = student_data)

# Create a route for the majors search page with GET
@app.route('/majors', methods = ['GET'])
def majors_get():
    # Get a list of majors
    list_of_majors = []
    # Get student data
    student_data = get_student_data('http://127.0.0.1:5000/api/students/all')
    for student in student_data:
        # If the major isn't already in the list, add it
        if student["major"] not in list_of_majors:
            list_of_majors.append(student["major"])
    # Sort alphabetically
    list_of_majors.sort()
    return render_template('majors.html', list_of_majors = list_of_majors)

# Create a route for the majors search page with POST
# When user clicks "Submit", the webpage goes to this method
@app.route('/majors', methods = ['POST'])
def majors_post():
    # Get a list of majors
    list_of_majors = []
    # Get student data
    student_data = get_student_data('http://127.0.0.1:5000/api/students/all')
    for student in student_data:
        # If the major isn't already in the list, add it
        if student["major"] not in list_of_majors:
            list_of_majors.append(student["major"])
    # Sort alphabetically
    list_of_majors.sort()

    # Get the form data
    major = request.form.get("major")
    print(major)
    # Create the request url to get students with that major
    url = f"http://127.0.0.1:5000/api/majors/{major}"
    # Send the request and get response
    result_list = get_student_data(url)
    # Send the results to the majors template

    return render_template('majors.html', list_of_majors = list_of_majors, result_list = result_list)

# Run the flask application
# We need port 5000 for the the other program, so we use port 5001 instead
app.run(port="5001")


