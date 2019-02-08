from flask import Flask
from flask_restful import Resource, reqparse
from ..models.models import parties, Parties, CreatePoliticalOffice, offices


from checks import checks             #to validate our data

#classes here represnt the different routes needed
#picks data structure from model



class Party(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('name', type=str, required=True, help='Fill in name')
    parser.add_argument('hqAddress', type=str, required=True, help='Fill in hqAddress')
    parser.add_argument('logoUrl', type=str, required=True, help='Fill in logoUrl')

#create party
    def post(self):
        party_data = Party.parser.parse_args()

        name = party_data['name']
        hqAddress = party_data['hqAddress']
        logoUrl = party_data['logoUrl']

        check = checks.Validations()

#validation of inputs
        if not check.validate_input_fields(name):
            return {"status": 400,
                    "Message": "Enter valid name"
                    }, 400
        if not check.validate_input_fields(hqAddress):
            return {"status": 400,
                    "Message": "Enter valid headquarter name"
                    }, 400
        if not check.validate_input_fields(logoUrl):
            return {"status": 400,
                    "Message": "Enter valid logoUrl"
                    }, 400

  #if party already exists
        party_name = Parties().get_party_by_name(name)
        if party_name:
            return {"status": 400,
                    "Message": "Party already exist"
                    }, 400


#adding party
        party = Parties(name, hqAddress, logoUrl)
        parties.append(party)
        if party:
            return {"status": 201,
                    "Message": "Party created successfully"
                    }, 201
        return {"status": 400,
                "Message": "Party not created"
                }, 400


#get all parties
    def get(self):
        return {"status": 200,
                "parties": [party.simplify() for party in parties]
                }


class GetSpecificParty(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,help='Please fill in this field')
    parser.add_argument('hqAddress', type=str, required=True,help='Please fill in this field')
    parser.add_argument('logoUrl', type=str, required=True, help='This field cant be empty')

    def get(self, id):
        party = Parties().get_specific_party_by_id(id)
        if not party:
            return {"status": 404,
                    "Message": "Party does not exist"
                    }, 404

        return {"party": party.simplify(),
                "status": 200
                }, 200

#delete specific id
    def delete(self, id):
        party = Parties().get_specific_party_by_id(id)

        if not party:
            return {"status": 404,
                    "message": "Party does not exist"
                    }, 404
        else:
            parties.remove(party)
            return {"status": 200,
                    "Message": "party deleted successfully"
                    }, 200


#update party by id
    def put(self, id):
        update_party = GetSpecificParty.parser.parse_args()
        name = update_party['name']
        hqAddress = update_party['hqAddress']
        logoUrl = update_party['logoUrl']

        check_data = checks.Validations()

        """check to see if the input strings are valid"""
        if not check_data.validate_input_fields(name):
            return {"status": 400,
                    "Message": "Enter valid name"
                    }, 400
        if not check_data.validate_input_fields(hqAddress):
            return {"status": 400,
                    "Message": "Enter valid hq name"
                    }, 400

        party = Parties().get_specific_party_by_id(id)
        if not party:
            return {
                "status": 404,
                "Message": "Party does not exist"
            },404
        else:
            party.name = name
            party.hqAddress = hqAddress
            party.logoUrl = logoUrl
            return {
                "message": "Party updated successfully",
                "status": 200,
                "Party": party.simplify()
            }, 200


class CreateOffice(Resource):

    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('name', type=str, required=True, help='Fill the name field')
    parser.add_argument('type', type=str, required=True, help='Fill the type field')

#get all offices
    def get(self):
        return {
            "status": 200,
            "Offices": [office.simplify() for office in offices]
        },200


#add office
    def post(self):

        office_data = CreateOffice.parser.parse_args()

        name = office_data['name']
        type = office_data['type']

        """ validate office data before submiiting """
        check_office = checks.Validations()

        if not check_office.validate_input_fields(name):
            return {"status": 400,
                    "Message": "Enter valid office name"
                    }, 400
        if not check_office.validate_input_fields(type):
            return {"status": 400,
                    "Message": "Enter valid office type"
                    }, 400

        office_exist = CreatePoliticalOffice().get_office_by_name(name)
        if office_exist:
            return {"Status": 400,
                    "Message": "Office name already exist"
                    }, 400

        office = CreatePoliticalOffice(name, type)
        offices.append(office)
        if office:
            return {"status": 201,
                    "Message": "New office created successfully"
                    }, 201


class GetSpecificOffice(Resource):
#specific office

    def get(self, office_id):

        office = CreatePoliticalOffice().get_office_by_id(office_id)

        if not office:
            return {"Status": 400,
                    "Message": "Office non-existent"
                    },400
        else:
            return {"status": 200,
                    "Office": office.simplify()
                    }, 200
