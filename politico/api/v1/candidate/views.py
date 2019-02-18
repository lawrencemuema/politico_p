from flask import Flask
from flask_restful import Resource, reqparse
from ..models.models import Candidates,Parties


from politico.checks import checks             #to validate our data

#classes here represnt the different routes needed
#picks data structure from model



class OfficeApply(Resource , Candidates,Parties):
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('candidate_name', type=str, required=True, help='Fill in canidates name')
    parser.add_argument('party', type=str, required=True, help='Fill in party name')
    parser.add_argument('office_id', type=int, required=True, help='Fill in office_id')

#register candidate
    def post(self):
        cand_data = OfficeApply().parser.parse_args()
        name = cand_data['candidate_name']
        party = cand_data['party']
        o_id = cand_data['office_id']

        check = checks.Validations()

#validation of inputs
        if not check.validate_input_fields(name):
            return {"status": 400,
                    "Message": "Enter valid name"
                    }, 400

  #if candidate already applied
        candidate_name = Candidates().get_name(name)
        if candidate_name:
            return {"status": 400,
                    "Message": "candidate already applied"
                    }, 400


#check if party exists
        party_name = Parties().get_name(party)

        if  party_name:
            # registering candidate party
            candidate = Candidates(name, party, o_id)
            candidate.register_candidates()
            if candidate:
                return {"status": 201,
                        "Message": "candidate registered successfully"
                        }, 201
            return {"status": 400,
                    "Message": "Candidate not registered"
                    }, 400

        return {"Message": "Party non existent"}, 400



#get all candidates
    def get(self):
        cands =Candidates().all_cands()
        return {"status": 200,
                "users": cands
                }, 200



class CandidateGet(Resource):


    # get specific candidate
    def get(self, c_id):
        cand = Candidates().get_id(c_id)
        if not cand:
            return {"status": 404,
                    "Message": "candidate does not exist"
                    }, 404

        return {"party": cand,
                "status": 200
                }, 200