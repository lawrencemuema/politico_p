import unittest
import json

from politico import app


class VotingTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

  #processing vote
    def test_voting(self):
        create_vote_data = {
            "candidate_name": "candidate1",
            "voter_id": "7",
            "office": "vice president"
        }
        res = self.client.post(
            "api/v1/vote",
            data=json.dumps(create_vote_data),
            headers={'content-type': 'application/json'}
        )
        return res

# invalid office_name
    def test_invalid_office(self):
        invalid_office_name = {
            "candidate_name": "candidate1",
            "voter_id": "7",
            "office": "vic92920"
        }
        res = self.client.post(
            "api/v1/vote",
            data=json.dumps(invalid_office_name),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)

#invalid voter id
    def test_invalid_voter_id(self):
        invalid_voter= {
            "candidate_name": "candidate1",
            "voter_id": "_2323<>",
            "office": "vice president"
        }
        res = self.client.post(
            "api/v1/vote",
            data=json.dumps(invalid_voter),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)



#invalid candidate name
    def test_invalid_candidate_name(self):
        create_invalid_candidate_name = {
            "candidate_name": "__()())&*2",
            "voter_id": "7",
            "office": "vice president"
        }
        res = self.client.post(
            "api/v1/vote",
            data=json.dumps(create_invalid_candidate_name),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 400)

