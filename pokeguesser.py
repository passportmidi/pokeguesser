import requests
from flask import Flask, render_template

# app is an instance of the Flask WSGI application class,
# so app is our WSGI application 
# argument: name of app's module or package
app = Flask(__name__)

@app.route("/") # tells Flask which URL triggers the hello_world() function
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/quiz")
def quiz():
    link = "https://archives.bulbagarden.net/media/upload/f/f7/0220Swinub.png"
    return render_template('quiz_template.html', pokeimg=link)

# for adding a form: 
# https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form#sending_form_data_to_your_web_server
# https://flask.palletsprojects.com/en/stable/tutorial/views/#login

# command to run app: pipenv run flask --app pokeguesser run