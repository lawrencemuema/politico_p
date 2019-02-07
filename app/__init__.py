""" Global Imports """
from flask import Flask, Blueprint
from flask_restful import Api, Resource

""" Importing Blueprints """
from .api.v1 import version_one as v1

""" local module imports """
from .api.v1.views import Party,Office,AllOffices,AllParties

""" creating an application instance """
def start_app():
   ## app = Flask(__name__, instance_relative_config=True)

    #app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')

    app = Flask(__name__)

    """ Registering application blueprint for admin views"""
    api = Api(v1)
    app.register_blueprint(v1, url_prefix='/api/v1')

    """ creating admin enpoints"""

    api.add_resource(Party, '/party/<int:p_id>')
    api.add_resource(AllParties, '/party')

    api.add_resource(Office, '/office/<int:o_id>')
    api.add_resource(AllOffices, '/office')


    return app