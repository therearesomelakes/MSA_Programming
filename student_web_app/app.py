from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

# Make a Flask app
app = Flask(__name__)
app.config["DEGBUG"] = True

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
    return render_template('index.html')


# Run the flask application
# We need port 5000 for the the other program, so we use port 5001 instead
app.run(port="5001")


