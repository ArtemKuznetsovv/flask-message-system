from functools import wraps
from flask import (
    jsonify,
    request,
)
import jwt
from werkzeug.exceptions import BadRequest
from message_system.models import User


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except BadRequest:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)

    return wrapper


def validate_body_params(*params):
    required = list(params)

    def decorator(fn):
        """Decorator that checks for the required parameters"""

        @wraps(fn)
        def wrapper(*args, **kwargs):
            missing = [r for r in required if r not in request.get_json()]
            if missing:
                response = {
                    "status": "error",
                    "message": "Request JSON is missing some required params",
                    "missing": missing
                }
                return jsonify(response), 400

            return fn(*args, **kwargs)

        return wrapper

    return decorator


def validate_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
            
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]

        if not token:
            return jsonify({"error": "Token is missing!"}), 401

        try:
            decoded_username = User.decode_auth_token(token)
            input_username = request.view_args["username"]
        except jwt.InvalidTokenError:
            return jsonify({"error": 'Token is invalid!'}), 401
        except KeyError:
            input_username = None

        if input_username is not None and input_username != decoded_username:
            return jsonify({"error": "Username doesn't match the given token!"}), 401

        return f(*args, **kwargs)

    return decorated
