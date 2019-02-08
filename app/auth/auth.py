from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
import datetime

from ..models.models import User, users
from checks import checks


class UserSignUp(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('firstname', type=str, required=True, help='Firstname is required')
    parser.add_argument('lastname', type=str, required=True, help='Lastname is required')
    parser.add_argument('othername', type=str, required=True, help='Othername is required')
    parser.add_argument('email', type=str, required=True,help='Email is required')
    parser.add_argument('phoneNumber', type=str, required=True, help='Number is required')
    parser.add_argument('passportUrl', type=str, required=True, help='PassportUrl is required')
    parser.add_argument('isAdmin', type=str, required=True, help='Accounttype is required')


    def post(self):
        user_data = UserSignUp().parser.parse_args()

        firstname = user_data['firstname']
        lastname = user_data['lastname']
        othername = user_data['othername']
        email = user_data['email']
        phoneNumber = user_data['phoneNumber']
        passportUrl = user_data['passportUrl']
        isAdmin = user_data['isAdmin']


#validate first
        validate_user_data = checks.Validations()

        if not validate_user_data.validate_input_fields(firstname):
            return {"status": 400,
                    "Message": "Please enter a valid firstname, with characters"
                    }, 400
        if not validate_user_data.validate_input_fields(lastname):
            return {"status": 400,
                    "Message": "Lastname, atleast 3 characters"
                    }, 400
        if not validate_user_data.validate_input_fields(othername):
            return {"status": 400,
                    "Message": "Othername should , atleast 3 characters"
                    }, 400
        if not validate_user_data.validate_email(email):
            return {"status": 400,
                    "Message": "Enter valid email address"
                    }, 400
        if not validate_user_data.validate_phone_number(phoneNumber):
            return {"status": 400,
                    "Message": "Phone number, 10 characters"
                    }, 400
        if not validate_user_data.validate_is_admin:
            return {"message": "Is admin field, between 0 and 1"
                    }, 400

        if not validate_user_data.validate_url(passportUrl):
            return {"status": 400,
                    "Message": "Enter valid passport url"
                    }, 400

 #user exists??????
        user_exist = User().get_user_by_email(email)
        if user_exist:
            return {"status": 400,
                    "Message": "This user already exist"
                    }, 400

        user = User(firstname, lastname, othername, email,
                    phoneNumber, passportUrl, bool(isAdmin))

        users.append(user)
        return {
                   "status": 201,
                   "Message": "Account created successfully"
               }, 201

#get all users

    def get(self):
        return {"status": 200,
                "users": [user.simplify() for user in users]
                }, 200



#login using firstname and email
class UserLogin(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('firstname', type=str, required=True, help='Firstname is required to login')
    parser.add_argument('email', type=str, required=True, help="The email is required to login")


    def post(self):
        login_data = UserLogin.parser.parse_args()

        firstname = login_data['firstname']
        email = login_data['email']

        validate_user_login = checks.Validations()

        if not validate_user_login.validate_input_fields(firstname):
            return {"status": 400,
                    "Message": "Please enter a valid firstname, with characters"
                    }, 404
        if not validate_user_login.validate_email(email):
            return {"status": 400,
                    "Message": "Please enter a valid email address"
                    }, 404

     #check if exists
        user_exist = User().get_user_by_email(email)
        if user_exist:
            return {
                       "Message": "Welcome you have successfully logged in",
                       "status": 200
                    }
        return {"status": 400,
                "Message": "Please enter a valid email address"
                }, 404