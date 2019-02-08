from datetime import datetime

parties = []
offices = []
users = []
vote = []
candidates = []
petition = []

#classes hold related data
#each class has initialization method for variable setup
#each class contains a simplify method to output in json format as a dictionary

class Parties:

    def __init__(self, name=None, hqAddress=None, logoUrl=None):
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.id = len(parties) + 1
        self.date_created = str(datetime.now().replace(microsecond=0, second=0))


    def simplify(self):
        return dict(
            id=self.id,
            name=self.name,
            hqAddress=self.hqAddress,
            logoUrl=self.logoUrl,
            date_created=self.date_created
        )

 # get party by name
    def get_party_by_name(self, name):
        for party in parties:
            if party.name == name:
                 return party

#get party by id
    def get_specific_party_by_id(self, id):
        for party in parties:
            if party.id == id:
                return party



class CreatePoliticalOffice:


    def __init__(self, name=None, Type=None):
        self.name = name
        self.Type = Type
        self.date_created = str(datetime.now().replace(microsecond=0, second=0))
        self.office_id = len(offices) + 1

    def simplify(self):
        return dict(
            id=self.office_id,
            name=self.name,
            type=self.Type,
            date_created=self.date_created
        )

    def get_office_by_name(self, office_name):
        for office in offices:
            if office.office_name == office_name:
                return office

    def get_office_by_id(self, office_id):
        for office in offices:
            if office.office_id == office_id:
                return office


class User:

    def __init__(

        self, firstname=None, lastname=None, othername=None, email=None, phoneNumber=None, passportUrl=None,
                 isAdmin=None):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.passportUrl = passportUrl
        self.isAdmin = isAdmin
        self.createdDate = str(datetime.now().replace(second=0, microsecond=0))
        self.user_id = len(users) + 1

    def simplify(self):
        return dict(
            firstname=self.firstname,
            lastname=self.lastname,
            othername=self.othername,
            email=self.email,
            phoneNumber=self.phoneNumber,
            passportUrl=self.passportUrl,
            isAdmin=self.isAdmin,
            createdDate=self.createdDate,
            user_id=self.user_id,

        )

    def get_user_by_email(self, email):
        for user in users:
            if user.email == email:
                return email





class Create_Candidates:


    def __init__(self, candidate=None, office_id=None, party_id=None):
        self.candidate = candidate
        self.office_id = office_id
        self.party_id = party_id
        self.candidate_id = len(candidates) + 1

    def simplify(self):
        return dict(
            id=self.candidate_id,
            candidate=self.candidate,
            office = self.office_id,
            party=self.party_id
        )

    def get_candidate_by_name(self, candidate_name):
        for candidate in candidates:
            if candidate.candidate_name == candidate_name:
                return candidate

    def get_candidate_by_id(self, candidate_id):
        for candidate in candidates:
            if candidate.candidate_id == candidate_id:
                return candidate