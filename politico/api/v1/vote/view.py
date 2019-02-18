from flask import Flask
from flask_restful import Resource, reqparse
from ..models.models import Vote, Candidates,Parties,CreateOffice, User


from politico.checks import checks             #to validate our data

#classes here represnt the different routes needed
#picks data structure from model



class VoteProcess(Resource ,Vote,Candidates,Parties,CreateOffice, User):
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('voter_id', type=int, required=True, help='Fill in office_id')
    parser.add_argument('candidate_name', type=str, required=True, help='Fill in canidates name')
    parser.add_argument('office', type=str, required=True, help='Fill in party name')


#register candidate
    def post(self):
        cand_data = VoteProcess().parser.parse_args()
        vo_id = cand_data['voter_id']
        name = cand_data['candidate_name']
        office = cand_data['office']


        check = checks.Validations()

#validation of inputs
        if not check.validate_input_fields(name):
            return {"status": 400,
                    "Message": "Enter valid candidate name"
                    }, 400

  #if voter already voted for same candidate/office already applied

        office = CreateOffice().get_name(office) #get office from office table


        if office: #if office exists in office table
            candidate_name = Candidates().get_name(name)  #get candidate from candidates table
            if candidate_name: #if candidate exists
                voterid = User().get_id(vo_id)  # get voter id from users table
                if voterid:  # if voter exists

                    # check if voter id with office voted for already exists
                    voteroffice = Vote().get_office_and_voterid(office, vo_id)
                    if voteroffice:
                        return {"Message": "voter already voted here"}, 400

                    vote = Vote(vo_id, name, office)
                    vote.register_vote()
                    if vote:
                        return {"status": 200,
                                "Message": "Vote processed"
                                }, 200

                return {"status": 400,
                        "Message": "voter not registered"
                        }, 400


            return  {"status": 400,
                    "Message": "Candidate not registered"
                    }, 400

        return {"Message": "Office non existent"}, 400


#get all candidates
    def get(self):
        all_v =Vote().all_votes()
        return {"status": 200,
                "users": all_v
                }, 200


#get individual voters
class Voter(Resource):


    def get(self, v_id):
        voters = Vote().get_id(v_id)
        if not voters:
            return {"status": 404,
                    "Message": "voter does not exist"
                    }, 404

        return {"party": voters,
                "status": 200
                }, 200


  #get individual candidates and results
class VotedCandidate(Resource):


    # get specific candidate
    def get(self, c_name):
        candv = Vote().get_candidate_voted(c_name)
        if not candv:
            return {"status": 404,
                    "Message": "candidate does not exist"
                    }, 404

        return {"party": candv,
                "status": 200
                }, 200