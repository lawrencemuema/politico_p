from flask import Blueprint
from .views import Parties

admin_blueprint = Blueprint('admin', __name__)