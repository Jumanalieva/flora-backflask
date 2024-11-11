import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from flask_migrate import Migrate
from models import db as root_db, ma  
from helpers import JSONEncoder
import logging
from dotenv import load_dotenv
import requests


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)
app.config.from_object(Config)  # Load configuration

# Enabling CORS for all routes in the app with specific settings
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}}, supports_credentials=True)


app.json_encoder = JSONEncoder


root_db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)  


app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)


logging.basicConfig(level=logging.DEBUG)


@app.route('/api/get_answer', methods=['POST'])
def get_answer():
    """
    Endpoint to process a user's query and fetch an answer from OpenAI API.
    """
   
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Query is missing"}), 400

   
    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini", 
        "messages": [{"role": "user", "content": user_query}],
        "temperature": 0.7
    }

    try:
       
        response = requests.post(openai_url, headers=headers, json=payload)
        response.raise_for_status()
        openai_response = response.json()

     
        return jsonify(openai_response)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error communicating with OpenAI API: {e}")
        return jsonify({"error": "Failed to communicate with OpenAI API"}), 500


if __name__ == '__main__':
    app.run(debug=True)  
