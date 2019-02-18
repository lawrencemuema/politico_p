from flask import Blueprint
from .user import UserSignUp

user_blueprint = Blueprint('user', __name__)