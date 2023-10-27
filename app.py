import os
from flask import Flask,flash, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from lib.database_connection import get_flask_database_connection
from lib.validation_tools import ValidationTools
from lib.user_repository import UserRepository
from lib.accommodation_repository import AccommodationRepository
from lib.listings_repository import ListingsRepository


tools = ValidationTools()

SPECIAL_CHARS = '!@*£&'
MIN_PASSWORD_LENGTH = 8

UPLOAD_FOLDER = './static/assets/accomodation_images'
ALLOWED_EXTENSIONS = {'jpg'}


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'

#  MAIN ROUTES #

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# # Creates the default route (homepage in this case)
@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('homepage.html')

# # Creates login route
@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

# # Creates the list accommodation route
@app.route('/create_listing', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/accommodations')
    return render_template('create_accommodation.html')

# # Creates about route
@app.route('/about', methods=['GET'])
def get_about():
    return render_template('about.html')

# # Creates terms and conditions route
@app.route('/terms', methods=['GET'])
def get_terms():
    return render_template('terms_and_conditions.html')

# # Creates request view route (placeholder for now)
@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('request_view.html')

# # Creates confirm request view (placeholder for now)
@app.route('/confirm', methods=['GET'])
def get_confirm():
    return render_template('request_confirmation.html')

# # Creates confirm request view (placeholder for now)
@app.route('/logout', methods=['GET'])
def get_logout():
    return render_template('logout.html')



# POST REQUESTS #


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
    

# GET REQUESTS #

# Creates the route for the accommodation list page
@app.route('/accommodations', methods=['GET','POST'])
def get_accommodations():

    connection = get_flask_database_connection(app)
    repository = ListingsRepository(connection)
    accommodations = repository.find_unbooked_unrequested_listings('2023-12-29','2023-12-30')
    return render_template('accommodations.html', accommodations=accommodations)

# Creates the route for an individual accomodation 
@app.route('/accommodations/<place_name>', methods=['GET'])
def get_accommodation_from_name(place_name):
    connection = get_flask_database_connection(app)
    repository = AccommodationRepository(connection)
    listingrepository = ListingsRepository(connection)
    accommodation = repository.find(place_name)
    dates = listingrepository.find_dates_blocked(9)
    return render_template('accommodation_page.html', accommodation=accommodation, dates=dates) #pass dates when time comes


# HTTP Method that gets user id and redirects to accomadation form Page
# It will be a get request --> we need user id
# we need to validate it 
# and then redirect 


@app.route('/test_date_accomodation')
def success():
    connection = get_flask_database_connection(app)
    listingrepository = ListingsRepository(connection)
    
    dates = listingrepository.find_dates_blocked(9)
    # check to see if user is in database 
    # if sucessful go to accomadation page
    # if unsuccessful go to login page
    
    # question : how do we get user input, will the data be persisted throughout the web app ? 
    # question : is it good practice to have user id passed through the url? 
    return render_template('date.html', dates = dates)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))