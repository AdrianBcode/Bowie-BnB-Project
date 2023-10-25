import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# Creates the default route (homepage in this case)
@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('homepage.html')

# Creates the route for accommodation list page
@app.route('/accommodations', methods=['GET'])
def get_accommodations():
    return render_template('accommodations.html')

# HTTP Method that gets user id and redirects to accomadation form Page
# It will be a get request --> we need user id
# we need to validate it 
# and then redirect 

@app.route('/post_accomodation/<user>')
def success(user):
    # check to see if user is in database 
    # if sucessful go to accomadation page
    # if unsuccessful go to login page

    # question : how do we get user input, will the data be persisted throughout the web app ? 
    # question : is it good practice to have user id passed through the url? 
    pass

@app.route('/post_accomodation/<user>', methods = ['POST'])
def new_accomodation():
    # this method will add the necessary information to the accomodations table, check table for the neccessary colunns, this is onclick after the form has been submitted
    pass 

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))