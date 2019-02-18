from flask_restful import Resource, reqparse
from flask import request, make_response, jsonify
from politico.checks import checks             #to validate our data
from ..models.models import User


class UserSignUp(Resource, User):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('firstname', type=str, required=True, help='Firstname is required')
    parser.add_argument('lastname', type=str, required=True, help='Lastname is required')
    parser.add_argument('othername', type=str, required=True, help='Othername is required')
    parser.add_argument('email', type=str, required=True,help='Email is required')
    parser.add_argument('phoneNumber', type=str, required=True, help='Number is required')
    parser.add_argument('passportUrl', type=str, required=True, help='PassportUrl is required')
    parser.add_argument('national_id', type=int, required=True, help='national_id is required (digits)')


    def post(self):
        user_data = UserSignUp().parser.parse_args()

        firstname = user_data['firstname']
        lastname = user_data['lastname']
        othername = user_data['othername']
        email = user_data['email']
        phoneNumber = user_data['phoneNumber']
        passportUrl = user_data['passportUrl']
        national_id = user_data['national_id']


#validate first
        validate_user_data = checks.Validations()

        if not validate_user_data.validate_input_fields(firstname):
            return {"Message": "Please enter a valid firstname"}, 400
        if not validate_user_data.validate_input_fields(lastname):
            return {"Message": "Please enter a valid lastname"}, 400
        if not validate_user_data.validate_input_fields(othername):
            return {"Message": "Please enter a valid othername"}, 400
        if not validate_user_data.validate_email(email):
            return {"Message": "Enter valid email address"}, 400
        if not validate_user_data.validate_phone_number(phoneNumber):
            return {"Message": "Please enter a valid phone number"}, 400
        if not validate_user_data.validate_input_fields(passportUrl):
            return {"Message": "Enter valid passport url"}, 400

 #user exists??????
        user_exist = User().get_email(email)
        if user_exist:
            return {"Message": "This user already exists"}, 400



        user = User(firstname,lastname,othername,email,phoneNumber,passportUrl,national_id)

        user.register_user()

        # users.append(user)
        if user:
            return {"status": 201,
                    "Message": "Account created successfully"
                    }, 201
        return {"status": 400,
                "Message": "Account not created"
                }, 400

#get all users

    def get(self):
        user =User().all_users()
        return {"status": 200,
                "users": user
                }, 200



#login using national id and email
class UserLogin(Resource , User):
    parser = reqparse.RequestParser()

    parser.add_argument('national_id', required=True, help='national id is required to login')
    parser.add_argument('email', type=str, required=True, help="email is required to login")


    def post(self):
        login_data = UserLogin.parser.parse_args()

        nat_id = login_data['national_id']
        email = login_data['email']

        validate_user_login = checks.Validations()

        if not validate_user_login.validate_email(email):
            return {"Message": "Please enter a registered email address"}, 404

     #check if exists
        user_exist = User().get_email(email)

        if user_exist:
            name_check = User().get_natID(nat_id)
            if name_check:
                return {
                           "Message": "Welcome to politico.",
                           "status": 200
                        }
            else:
                return {"status": 400,
                        "Message": "User not found, enter valid national id"
                        }, 404
        else:
            return {"status": 400,
                "Message": "Sorry, email not associated with any user"
                }, 404