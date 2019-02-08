import unittest
import json

from app import create_app


class PoliticalParties(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

  #party creation
    def test_party_creation(self):
        create_party_data = {
            "name": "odm",
            "hqAddress": "Nairobi",
            "logoUrl": "img.png"
        }
        res = self.client.post(
            "api/v1/party",
            data=json.dumps(create_party_data),
            headers={'content-type': 'application/json'}
        )
        return res


  #invalid hq entry
    def test_invalid_party_hqaddress(self):
        create_invalid_party_hqaddres = {
            "name": "jubilee",
            "hqAddress": "1234567890",
            "logoUrl": "img1.png"
        }
        res = self.client.post(
            "api/v1/party",
            data=json.dumps(create_invalid_party_hqaddres),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)


#invalid logo url
    def test_invalid_logo_url(self):
        invalid_logo_url = {
            "name": "jubilee",
            "hqAddress": "Niarobi",
            "logoUrl": "111111"
        }
        res = self.client.post(
            "api/v1/party",
            data=json.dumps(invalid_logo_url),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)



#invalid party name
    def test_invalid_party_data(self):
        create_invalid_party_name = {
            "name": "123",
            "hqAddress": "Niarobi",
            "logoUrl": "localhost/images/img1.png"
        }
        res = self.client.post(
            "api/v1/party",
            data=json.dumps(create_invalid_party_name),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)

