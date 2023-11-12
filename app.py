from flask import Flask, render_template, request
import requests

# setup
app = Flask(__name__)

@app.route("/")
def base():
    """ Displays homepage """
    context = {}
    
    return render_template("base.html", **context)