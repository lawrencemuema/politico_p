from views import Party,Office,AllOffices,AllParties
from flask import Blueprint



#versioning
version_one = Blueprint('api_v1', __name__, url_prefix = '/api/v1')

