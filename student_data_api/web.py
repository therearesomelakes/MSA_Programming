import flask
from flask import request, jsonify

# Create a flask app object
app = flask.Flask(__name__)
# App refers to a flask object.  Flask is a server that users can connecto to and ask for information

# Tell the server to reload each time the code changes
app.config["DEBUG"] = True

# Load student dictionaries 

# Create a route to display our name
@app.route('/', methods = ['GET'])
def index():
    return "<h1> My name is Steven Shaw </h1>"

# Create 2 routes
    # Return all student data
    # return students by major

# Run application
app.run()