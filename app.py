from flask import Flask, render_template, request
import requests

# setup
app = Flask(__name__)
API_URL = "https://swapi.py4e.com/api/"

def format_character_results(func):
    def wrapper(character_id):
        try:
            result_json = func(character_id)
            formatted_results = {
                "name": result_json['name'],
                "height": result_json['height'],
                "mass": result_json['mass'],
                "hair_color": result_json['hair_color'],
                "eye_color": result_json['eye_color']
            }
            return formatted_results
        except KeyError:
            # API response doesn't match the expected structure
            error_message = f"Error: Character with ID {character_id} not found or API response structure is unexpected."
            return {"error": error_message}
    return wrapper

@format_character_results
def get_character(character_id: str):
    """Returns character data from the Star Wars API."""
    API_URL = "https://swapi.py4e.com/api/people/" + character_id
    result_json = requests.get(API_URL).json()
    return result_json

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
    # get character data
    character = get_character(character_id)

    context = {
        "character": character,
    }

    return render_template("character_results.html", **context)