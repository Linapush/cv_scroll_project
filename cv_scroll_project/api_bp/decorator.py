import jwt
from flask import request, abort, current_app, jsonify
from models import User
from functools import wraps
from werkzeug.security import check_password_hash
from flask_login import current_user

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Проверить, существует ли заголовок authorization"""

        if "Authorization" in request.headers:
            token = request.headers.get('Authorizarion')
            if token:
                try:
                    data = jwt.decode(token, current_app.secret_key, algorithms=['HS256'])
                    user = User.query.filter(User.email == data["email"]).first()
                    if not user:
                        return {"message":"user not found"}, 401
                    if not check_password_hash(user.password, data["password"]):
                        return {"message":"password invalid"}
                    
                except Exception as e:
                    return {"message": "Invalid token", "error": e}, 401
            else:
                return {"message": "Authentication token required"}, 401
        else:
            return {"message": "Authorization required"}, 401
            # return abort(401)
        return func(*args, **kwargs)
    
    return wrapper

def roles_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.has_role(role):  
                return jsonify({"message": "Access denied"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return wrapper