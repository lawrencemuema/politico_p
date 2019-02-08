""" Global Imports """
from flask import Flask, Blueprint
from flask_restful import Api


from .admin import admin_blueprint as admin_blp
from .admin.views import Party, GetSpecificParty, CreateOffice, GetSpecificOffice



def create_app():
    app = Flask(__name__)
    admins = Api(admin_blp)

    app.register_blueprint(admin_blp, url_prefix='/api/v1')


    """ creating admin endpoints"""
    admins.add_resource(Party,'/party')
    admins.add_resource(GetSpecificParty, '/party/<int:id>')
    admins.add_resource(CreateOffice, '/office')
    admins.add_resource(GetSpecificOffice, '/office/<int:office_id>')



    return app