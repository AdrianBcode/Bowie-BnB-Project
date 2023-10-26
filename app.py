import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.validation_tools import ValidationTools
from lib.user_repository import UserRepository
from lib.accommodation_repository import AccommodationRepository


tools = ValidationTools()

SPECIAL_CHARS = '!@*£&'
MIN_PASSWORD_LENGTH = 8

# Create a new Flask app
app = Flask(__name__)

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# # Creates the default route (homepage in this case)
@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('homepage.html')

# # Post request for form on user signup page
@app.route('/', methods=['POST'])
def add_new_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if tools.password_validator(password,SPECIAL_CHARS,MIN_PASSWORD_LENGTH):
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        repository.create(name,email,password)
        return redirect(f'/accommodations')
    else:
        return 'Please input a valid string inputfor all values', 400
    

# Creates the route for the accommodation list page
@app.route('/accommodations', methods=['GET'])
def get_accommodations():
    connection = get_flask_database_connection(app)
    repository = AccommodationRepository(connection)
    accommodations = repository.all()
    return render_template('accommodations.html', accommodations=accommodations)

# Creates the route for an individual accomodation 
@app.route('/accommodations/<place_name>', methods=['GET'])
def get_accommodation_from_name(place_name):
    connection = get_flask_database_connection(app)
    repository = AccommodationRepository(connection)
    accommodation = repository.find(place_name)
    return render_template('accommodation_page.html', accommodation=accommodation)


# HTTP Method that gets user id and redirects to accomadation form Page
# It will be a get request --> we need user id
# we need to validate it 
# and then redirect 

# @app.route('/post_accomodation/<user>')
# def success(user):
#     # check to see if user is in database 
#     # if sucessful go to accomadation page
#     # if unsuccessful go to login page

#     # question : how do we get user input, will the data be persisted throughout the web app ? 
#     # question : is it good practice to have user id passed through the url? 
#     pass

# @app.route('/post_accomodation/<user>', methods = ['POST'])
# def new_accomodation():
#     # this method will add the necessary information to the accomodations table, check table for the neccessary colunns, this is onclick after the form has been submitted
#     pass 

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))