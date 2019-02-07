from flask import Flask , request, jsonify, make_response
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

#lists
parties = []
offices = []
users = []
candidates = []
vote = []
petition = []

#class for adding and viewing all parties
class AllParties(Resource):
    def get(self):
        return make_response(jsonify({
            "Status": 2,
            "data": parties
        }), 200)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("logoUrl")
        args = parser.parse_args()


        new_party = {
            "id": len(parties) + 1,
            "name": args["name"],
            "logoUrl": args["logoUrl"]
        }
        parties.append(new_party)
        return make_response(jsonify({
            "status": 1,
            "data": new_party
        }), 201)

#class for viewing specific party, editing and deleting
class Party(Resource):
    def get(self, p_id):
        for party in parties:
            if p_id == party["id"]:
                return make_response(jsonify({
                    "Status": 3,
                    "data": party
                }), 200)
        return make_response(jsonify({
            "Status": 404,
            "error": "specific party not found"
        }), 404)



    def put(self, p_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("logoUrl")
        args = parser.parse_args()

        for party in parties:

            if p_id != party["id"]:
                return make_response(jsonify({
                    "Status": 404,
                    "error": "party could not be updated"
                }), 404)
            elif p_id == party["id"]:
                party["name"] = args["name"]
                return party, 200

        updated_party = {
            "name": args["name"],
            "id": p_id,
            "logoUrl": args["logoUrl"]
        }
        parties.append(updated_party)

        return make_response(jsonify({
            "status": 5,
            "data": updated_party
        }), 201)



    def delete(self, p_id):
        global parties
        parties = [party for party in parties if party["id"] != p_id]
        return make_response(jsonify({
            "status": 00,
            "message": "party {} is deleted.".format(p_id)
        }), 201)


#class for adding and viewing all offices
class AllOffices(Resource):
    def get(self):
        return make_response(jsonify({
            "Status": "ok",
            "data": offices
        }), 200)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("type")
        args = parser.parse_args()


        new_office = {
            "id": len(offices) + 1,
            "name": args["name"],
            "type": args["type"]
        }
        offices.append(new_office)
        return make_response(jsonify({
            "status": 2,
            "data": new_office
        }), 201)

#class for viewing specific office
class Office(Resource):
    def get(self, o_id):
        for office in offices:
            if o_id == office["id"]:
                return make_response(jsonify({
                    "Status": "ok",
                    "data": office
                }), 200)
        return make_response(jsonify({
            "Status": 404,
            "error": "specific party not found"
        }), 404)

