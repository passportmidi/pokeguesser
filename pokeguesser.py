import requests
import random
from flask import Flask, render_template
import pokeapi

# app is an instance of the Flask WSGI application class,
# so app is our WSGI application 
# argument: name of app's module or package
app = Flask(__name__)

@app.route("/") # tells Flask which URL triggers the hello_world() function
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/quiz")
def quiz():
    pokemon = pokeapi.get_random_pokemon()
    img = pokemon["sprites"]["other"]["official-artwork"]["front_default"]
    return render_template('quiz_template.html', pokeimg=img)