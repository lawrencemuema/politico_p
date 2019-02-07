import unittest
import json
from app import start_app

class TestPolitico(unittest.TestCase):

    #setup for app and data

    def setUp(self):
        self.app = start_app()
        self.client = self.app.test_client()
        self.partydata = {
            "name": "mutu",
            "logoUrl": "else.png"
        }
        self.editp = {
             "name": "mutu22",
            "logoUrl": "else.png"
        }
        self.office_data = {
            "name": "governor",
            "type": "federal"
        }

    def post(self, path='/party', data={}):
        if not data:
            data = self.partydata

        resp = self.client.post(path='/party', data=json.dumps(self.partydata), content_type='application/json')
        return resp
    def post2(self, path='/office', data={}):
        if not data:
            data = self.office_data

        resp = self.client.post(path='/office', data=json.dumps(self.office_data), content_type='application/json')
        return resp


    def test_adding_party(self):
        resp = self.post()
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.json['data'])
        self.assertEqual(resp.json['status'], 1)

    def test_get_all_parties(self):
        resp = self.client.get(path='/party', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json['data'])

    def test_get_single_party(self):
        resp = self.client.get(path='/party/1', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json['data'])

    def test_edit_party(self):
        response = self.client.put(path='/party/1', data=json.dumps(self.editp), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json['data'])
        self.assertEqual(response.json['status'], 5)

    def test_delete_party(self):
        response = self.client.delete(path='/party/1', content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['status'], 0)








####test office

    def test_adding_office(self):
        resp = self.post2()
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.json['data'])
        self.assertEqual(resp.json['status'], 2)

    def test_get_all_offices(self):
        resp = self.client.get(path='/office', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json['data'])

    def test_get_single_office(self):
        resp = self.client.get(path='/office/1', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.json['data'])

if __name__ == '__main__':
    unittest.main()