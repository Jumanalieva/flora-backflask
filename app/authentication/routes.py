import os
from flask import Blueprint, redirect, request, url_for, session, flash
from urllib.parse import urlencode
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

auth = Blueprint('auth', __name__)

# Retrieve the Cognito variables from the environment
COGNITO_CLIENT_ID = os.getenv('COGNITO_CLIENT_ID')
COGNITO_REDIRECT_URI = os.getenv('COGNITO_REDIRECT_URI')  # Add this variable to your .env
COGNITO_DOMAIN = os.getenv('COGNITO_DOMAIN')  # Add this variable to your .env

@auth.route('/signup')
def signup():
    # Redirects user to Cognito's hosted sign-up page
    query_params = {
        "response_type": "code",
        "client_id": COGNITO_CLIENT_ID,
        "redirect_uri": COGNITO_REDIRECT_URI,
        "scope": "email openid profile"
    }
    signup_url = f"{COGNITO_DOMAIN}/signup?{urlencode(query_params)}"
    return redirect(signup_url)

@auth.route('/signin')
def signin():
    # Redirects user to Cognito's hosted sign-in page
    query_params = {
        "response_type": "code",
        "client_id": COGNITO_CLIENT_ID,
        "redirect_uri": COGNITO_REDIRECT_URI,
        "scope": "email openid profile"
    }
    signin_url = f"{COGNITO_DOMAIN}/login?{urlencode(query_params)}"
    return redirect(signin_url)

