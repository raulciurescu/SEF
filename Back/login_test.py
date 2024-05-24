import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from Routes.Login import Login_route

class TestLoginRoute(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(Login_route)
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_manager_login(self):
        # Mocking the database response
        with patch('pymongo.collection.Collection.find_one') as mock_find_one:
            mock_find_one.return_value = {"ManagerEmail": "manager@example.com", "ManagerPassword": "password123"}
            
            # Make a POST request to the login route
            response = self.app.post('/Login', json={"email": "manager@example.com", "pwd": "password123"})

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], "Manager")

    def test_staff_login(self):
        # Mocking the database response
        with patch('pymongo.collection.Collection.find_one') as mock_find_one:
            mock_find_one.return_value = {"StaffEmail": "staff@example.com", "StaffPassword": "password123", "StaffID": 123}
            
            # Make a POST request to the login route
            response = self.app.post('/Login', json={"email": "staff@example.com", "pwd": "password123"})

            # Assert the response
            self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        # Mocking the database response
        with patch('pymongo.collection.Collection.find_one') as mock_find_one:
            mock_find_one.return_value = None
            
            # Make a POST request to the login route with invalid credentials
            response = self.app.post('/Login', json={"email": "invalid@example.com", "pwd": "invalidpassword"})

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], "Invalid email or password")

if __name__ == "__main__":
    unittest.main()
