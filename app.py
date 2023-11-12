from flask import Flask, render_template, request
import requests

# setup
app = Flask(__name__)
API_URL = "https://swapi.py4e.com/api/"

def get_character(character_id: str):
    """Returns json data for the character."""
    
    API_URL = "https://swapi.py4e.com/api/people/" + character_id
    result_json = requests.get(API_URL).json()
    return result_json

def format_character_results(result_json):
    """Returns formatted dictionary for character_results"""
    
    results = {
        "name": result_json['name'],
        "height": result_json['height'],
        "mass": result_json['mass'],
        "hair_color": result_json['hair_color'],
        "eye_color": result_json['eye_color']
    }
    
    print(results)
    return results

@app.route("/")
def home():
    """ Displays homepage """
    context = {}
    
    return render_template("home.html", **context)

@app.route("/character-results")
def results():
    """Displays results for the character."""

    # get character ID
    character_id = str(request.args.get("character-id"))
    
    character_results = get_character(character_id)
    formatted_character_results = format_character_results(character_results)

    context = {
        "formatted_character_results": formatted_character_results,
    }
    print(context)

    return render_template("character_results.html", **context)