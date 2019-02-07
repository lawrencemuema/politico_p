from flask import Blueprint
from flask_restful import Api, Resource
from views import *


#versioning
version_one = Blueprint('api_v1', __name__, url_prefix = '/api/v1')
api = Api(version_one)


api.add_resource(Party, '/party/<int:p_id>')
api.add_resource(AllParties, '/party')

api.add_resource(Office, '/office/<int:o_id>')
api.add_resource(AllOffices, '/office')
