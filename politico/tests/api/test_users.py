import unittest
import json

from politico import app


class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def create_account(self):
        user_data = {
            "firstname": "lawrence",
            "lastname": "maxwel",
            "othername": "muema",
            "email": "user@pol.com",
            "phoneNumber": "0712345678",
            "passportUrl": "http://localhost.com/img1.png",
            "national_id": "33196490"


        }
        response = self.client.post(
            "api/v1/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        return response

    def user_login(self):
        login_data = {
            "national_id": "33196490",
            "email": "user@pol.com"
        }
        response = self.client.post(
            "api/v1/signin",
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
            "firstname": "lawrence",
            "lastname": "maxwel",
            "othername": "muema",
            "email": "user@pol.com",
            "phoneNumber": "0712345678",
            "passportUrl": "http://localhost.com/img1.png",
            "national_id": "33196490"
        }

        self.create_account()
        response = self.client.post(
            "api/v1/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)


    def test_user_does_not_exist_sign_up(self):
        login_data = {
            "national_id": "00000",
            "email": "smth@gmail.com"
        }
        self.create_account()
        response = self.client.post(
            "api/v1/signin",
            data=json.dumps(login_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 404)

    def test_invalid_email(self):
        user_data = {
            "firstname": "lawrence",
            "lastname": "maxwel",
            "othername": "muema",
            "email": "@@@pol.com",
            "phoneNumber": "0712345678",
            "passportUrl": "http://localhost.com/img1.png",
            "national_id": "33196490"
        }
        response = self.client.post(
            "api/v1/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_firstname(self):
        user_data = {
            "firstname": "+<@>@22",
            "lastname": "maxwel",
            "othername": "muema",
            "email": "user@pol.com",
            "phoneNumber": "0712345678",
            "passportUrl": "http://localhost.com/img1.png",
            "national_id": "33196490"
        }
        response = self.client.post(
            "api/v1/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)


    def test_invalid_lastname(self):
        user_data = {
            "firstname": "lawrence",
            "lastname": "$%><>?+",
            "othername": "muema",
            "email": "user@pol.com",
            "phoneNumber": "0712345678",
            "passportUrl": "http://localhost.com/img1.png",
            "national_id": "33196490"
        }
        response = self.client.post(
            "api/v1/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_othernames(self):
        user_data = {
            "firstname": "lawrence",
            "lastname": "maxwel",
            "othername": ")__?)>90",
            "email": "user@pol.com",
            "phoneNumber": "0712345678",
            "passportUrl": "http://localhost.com/img1.png",
            "national_id": "33196490"
        }
        response = self.client.post(
            "api/v1/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)


    def test_invalid_phone_number(self):
        user_data = {
            "firstname": "lawrence",
            "lastname": "maxwel",
            "othername": "muema",
            "email": "user@pol.com",
            "phoneNumber": "07678",
            "passportUrl": "http://localhost.com/img1.png",
            "national_id": "33196490"
        }
        response = self.client.post(
            "api/v1/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

    def test_invalid_url(self):
        user_data = {
            "firstname": "lawrence",
            "lastname": "maxwel",
            "othername": "muema",
            "email": "user@pol.com",
            "phoneNumber": "0712345678",
            "passportUrl": "img.png",
            "national_id": "33196490"
        }
        response = self.client.post(
            "api/v1/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)





