import unittest
import json

from app import create_app


class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def create_account(self):
        user_data = {
            "firstname": "wila",
            "lastname": "male",
            "othername": "user",
            "email": "user@gmail.com",
            "phoneNumber": "0712345678",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": 0
        }
        response = self.client.post(
            "api/v1/user/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        return response

    def user_login(self):
        login_data = {
            "firstname": "wila",
            "email": "user@gmail.com"
        }
        response = self.client.post(
            "api/v1/user/signin",
            data=json.dumps(login_data),
            headers={"content-type": "application/json"}
        )
        return response

    def test_signin(self):
        self.create_account()
        response = self.user_login()

        self.assertEqual(response.status_code, 200)

    def test_user_email_exists(self):

        user_data = {
            "firstname": "wila",
            "lastname": "male",
            "othername": "user",
            "email": "user@gmail.com",
            "phoneNumber": "0712345678",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": 0
        }

        self.create_account()
        response = self.client.post(
            "api/v1/user/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)


    def test_user_does_not_exist_sign_up(self):
        login_data = {
            "firstname": "lawi",
            "email": "gmail.com"
        }
        self.create_account()
        response = self.client.post(
            "api/v1/user/signin",
            data=json.dumps(login_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 404)

    def test_invalid_email(self):
        user_data = {
            "firstname": "wila",
            "lastname": "male",
            "othername": "user",
            "email": "@@#mm@.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": 0
        }
        response = self.client.post(
            "api/v1/user/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_firstname(self):
        user_data = {
            "firstname": "%43*****mmm",
            "lastname": "wila",
            "othername": "user",
            "email": "user@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": 0
        }
        response = self.client.post(
            "api/v1/user/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)


    def test_invalid_lastname(self):
        user_data = {
            "firstname": "john",
            "lastname": "88989098",
            "othername": "user",
            "email": "user@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": 0
        }
        response = self.client.post(
            "api/v1/user/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_othernames(self):
        user_data = {
            "firstname": "john",
            "lastname": "lastaname",
            "othername": "^hgf99",
            "email": "user@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": 0
        }
        response = self.client.post(
            "api/v1/user/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)


    def test_invalid_phone_number(self):
        user_data = {
            "firstname": "john",
            "lastname": "lastaname",
            "othername": "othernames",
            "email": "user@gmail.com",
            "phoneNumber": "kk445-862ll",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": 0
        }
        response = self.client.post(
            "api/v1/user/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_url(self):
        user_data = {
            "firstname": "john",
            "lastname": "lastaname",
            "othername": "othernames",
            "email": "user@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "localhost.com/img1.png",
            "isAdmin": 1
        }
        response = self.client.post(
            "api/v1/user/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)





