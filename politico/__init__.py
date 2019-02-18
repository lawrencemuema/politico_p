from flask import Flask, Blueprint
from flask_restful import Api
from .db_config import DbSetup

app = Flask(__name__)

from .api.v1.ebody import admin_blueprint as admin_blp
from .api.v1.user import user_blueprint as user_blp
from .api.v1.candidate import cand_blueprint as can_blp
from .api.v1.vote import vote_blueprint as v_blp


from .api.v1.ebody.views import *
from .api.v1.candidate.views import *
from .api.v1.user.user import *
from .api.v1.vote.view import *





body = Api(admin_blp)
user = Api(user_blp)
cand = Api(can_blp)
vote = Api(v_blp)


database = DbSetup()
database.create_tables()

    #registering blueprints
app.register_blueprint(admin_blp, url_prefix='/api/v1')
app.register_blueprint(user_blp, url_prefix='/api/v1')
app.register_blueprint(can_blp, url_prefix='/api/v1')
app.register_blueprint(v_blp, url_prefix='/api/v1')

""" creating admin endpoints"""
body.add_resource(Party,'/party')
body.add_resource(GetSpecificParty, '/party/<int:id>')
body.add_resource(CreateOffice2, '/office')
body.add_resource(GetSpecificOffice, '/office/<int:office_id>')

""" creating user endpoints"""
user.add_resource(UserSignUp, '/signup')
user.add_resource(UserLogin, '/signin')

""" creating candidate endpoints"""
cand.add_resource(OfficeApply, '/apply')
cand.add_resource(CandidateGet, '/apply/<int:c_id>')


""" creating voting endpoints"""
vote.add_resource(VoteProcess, '/vote')
vote.add_resource(VotedCandidate, '/vote/<c_name>')
vote.add_resource(Voter, '/vote/<int:v_id>')