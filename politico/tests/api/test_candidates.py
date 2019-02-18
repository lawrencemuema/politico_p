import unittest
import json

from politico import app


class CandidatesTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

  #aplication
    def test_application(self):
        create_cand_data = {
            "candidate_name": "candidate2",
            "party": "party1",
            "office_id": "3"
        }
        res = self.client.post(
            "api/v1/apply",
            data=json.dumps(create_cand_data),
            headers={'content-type': 'application/json'}
        )
        return res

# invalid office_id
    def test_invalid_office_id(self):
        invalid_office_id = {
            "candidate_name": "candidate2",
            "party": "party1",
            "office_id": "myoffice"
        }
        res = self.client.post(
            "api/v1/apply",
            data=json.dumps(invalid_office_id),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)

#invalid party
    def test_invalid_party(self):
        invalid_party = {
            "candidate_name": "candidate2",
            "party": "0101010",
            "office_id": "3"
        }
        res = self.client.post(
            "api/v1/apply",
            data=json.dumps(invalid_party),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)



#invalid office name
    def test_invalid_candidate_data(self):
        create_invalid_candidate_name = {
            "candidate_name": "00019",
            "party": "party1",
            "office_id": "3"
        }
        res = self.client.post(
            "api/v1/apply",
            data=json.dumps(create_invalid_candidate_name),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)

