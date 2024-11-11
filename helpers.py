# from functools import wraps
# import secrets
# from flask import request, jsonify
# from models import User
# import decimal
# import json

# def token_required(our_flask_function):
#     @wraps(our_flask_function)
#     def decorated(*args, **kwargs):
#         token = None

#         # Extract token from header
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token'].split(' ')[1]

#         if not token:
#             return jsonify({'message': 'Token is missing.'}), 401

#         # Query User and validate token
#         current_user_token = User.query.filter_by(token=token).first()
#         if not current_user_token or not secrets.compare_digest(token, current_user_token.token):
#             return jsonify({'message': 'Token is invalid'}), 401

#         # Proceed with function if token is valid
#         return our_flask_function(current_user_token, *args, **kwargs)
#     return decorated


# class JSONEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, decimal.Decimal):
#             # Convert decimal instances into strings for JSON compatibility
#             return str(obj)
#         return super(JSONEncoder, self).default(obj)
import decimal
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances into strings for JSON compatibility
            return str(obj)
        return super(JSONEncoder, self).default(obj)
