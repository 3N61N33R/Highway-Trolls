import unittest
import json

from app import app

class TestUser(unittest.TestCase):
    def setUp(self):
        """Creates the app as a test client"""
        app.testing = True
        self.app = app.test_client()

    def register_user(self):
        user_info ={
            "full-name": "Gray Vianne",
            "email": "grayvianne@gmail.com",
            "password":"Nm643Power"

        }
        response = self.app.post('/api/v1/auth/register',
            data= json.dumps(user_info),
            content_type = 'application/json')
        return response

    def test_user_registration(self):
        response = self.register_user()
	self.assertEqual(response.status_code, 201)
	self.assertEqual(response.status_code, 200)

    def login_user(self):
        login_info ={
            "email": "grayvianne@gmail.com",
            "password":"Nm643Power"
        }
        response = self.app.post('/api/v1/auth/register',
            data= json.dumps(login_info),
            content_type = 'application/json')
        return response

    def test_login(self):
        response = self.login_user()
        self.assertEqual(response.status_code, 200)
	

if __name__ == "__main__":
	unittest.main()
