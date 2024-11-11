import os
import boto3
import base64
import json
from dotenv import load_dotenv
from botocore.exceptions import ClientError

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

def get_secret():
    secret_name = "rds!db-5036d407-b8e6-40ff-bed6-34aabb503c4a"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        print(f"Error retrieving secret: {e}")
        raise e

    # Parse the secret string as JSON and return it
    secret = get_secret_value_response['SecretString']
    return json.loads(secret)

class Config:
    """
    Set config variables for the Flask app using environment variables where available.
    """

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Attempt to load database credentials from AWS Secrets Manager
    try:
        secrets = get_secret()
        DB_HOST = secrets.get('host')
        DB_PORT = secrets.get('port', '5432')  # Default to 5432 for PostgreSQL
        DB_NAME = secrets.get('dbname')
        DB_USER = secrets.get('username')
        DB_PASSWORD = secrets.get('password')
    except Exception as e:
        print(f"Failed to load secrets from Secrets Manager, using defaults. Error: {e}")
        DB_HOST = os.getenv('DB_HOST')
        DB_PORT = os.getenv('DB_PORT', '5432')
        DB_NAME = os.getenv('DB_NAME')
        DB_USER = os.getenv('DB_USER')
        DB_PASSWORD = os.getenv('DB_PASSWORD')

    # Set up the SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        if DB_HOST and DB_NAME and DB_USER and DB_PASSWORD
        else 'sqlite:///' + os.path.join(basedir, 'app.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AWS Cognito
    COGNITO_CLIENT_ID = os.getenv('COGNITO_CLIENT_ID')
    COGNITO_USER_POOL_ID = os.getenv('COGNITO_USER_POOL_ID')
    COGNITO_REGION = os.getenv('COGNITO_REGION')

