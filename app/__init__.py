from flask import Flask
from flask_restful import Api, Resource
from .api.v1.views import Party, AllOffices,AllParties,Office




def start_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Party, '/party/<int:p_id>')
    api.add_resource(AllParties, '/party')

    api.add_resource(Office, '/office/<int:o_id>')
    api.add_resource(AllOffices, '/office')

    return app