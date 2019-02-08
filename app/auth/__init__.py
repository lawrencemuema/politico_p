from flask import Blueprint
from .auth import UserSignUp

user_blueprint = Blueprint('user', __name__)