import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from Routes.Staff import Staff_route

class TestStaffRoute(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(Staff_route)
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_add_staff(self):
        # Mocking the database insert_one method
        with patch('pymongo.collection.Collection.insert_one') as mock_insert_one:
            # Simulate a successful insertion
            mock_insert_one.return_value = True

            # Make a POST request to add a new staff member
            response = self.app.post('/Staff', json={
                "StaffID": "123",
                "StaffName": "John Doe",
                "StaffEmail": "john@example.com",
                "StaffPassword": "password123"
            })

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], "Staff added")

    def test_get_staff(self):
        # Mocking the database find method
        with patch('pymongo.collection.Collection.find') as mock_find:
            # Simulate finding staff members
            mock_find.return_value = [
                {"_id": "1", "StaffID": "123", "StaffName": "John Doe", "StaffEmail": "john@example.com", "StaffPassword": "encrypted_password"}
            ]

            # Make a GET request to retrieve staff members
            response = self.app.get('/Staff')

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            self.assertEqual(response.json[0]["StaffID"], "123")
            self.assertEqual(response.json[0]["StaffName"], "John Doe")
            self.assertEqual(response.json[0]["StaffEmail"], "john@example.com")

    def test_delete_staff(self):
        # Mocking the database delete_one method
        with patch('pymongo.collection.Collection.delete_one') as mock_delete_one:
            # Simulate a successful deletion
            mock_delete_one.return_value = True

            # Make a DELETE request to delete a staff member
            response = self.app.delete('/Staff1/123')

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], "Staff deleted")

if __name__ == "__main__":
    unittest.main()
