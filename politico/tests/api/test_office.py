import unittest
import json

from politico import app


class PoliticalOffices(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

  #office creation
    def test_office_creation(self):
        create_office_data = {
            "name": "governor",
            "type": "local"
        }
        res = self.client.post(
            "api/v1/office",
            data=json.dumps(create_office_data),
            headers={'content-type': 'application/json'}
        )
        return res

#invalid type
    def test_invalid_type(self):
        invalid_type = {
            "name": "governor",
            "type": "111111"
        }
        res = self.client.post(
            "api/v1/office",
            data=json.dumps(invalid_type),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)



#invalid office name
    def test_invalid_office_data(self):
        create_invalid_office_name = {
            "name": "123",
            "type": "federal"
        }
        res = self.client.post(
            "api/v1/office",
            data=json.dumps(create_invalid_office_name),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)

