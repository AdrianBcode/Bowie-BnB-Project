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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
