import unittest
from flask import Flask
from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# Import the blueprint
from Routes.ClientReservations import ClientReservation_route

class ClientReservationTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Flask test client
        cls.app = Flask(__name__)
        cls.app.register_blueprint(ClientReservation_route)
        cls.client = cls.app.test_client()

        # Set up the test database connection
        cls.client_db = MongoClient('localhost', 27017)
        cls.db = cls.client_db['FullAppSef']
        cls.collection = cls.db['Reservations']

    @classmethod
    def tearDownClass(cls):
        # Tear down the test database connection
        cls.client_db.close()

    def setUp(self):
        # Ensure the collection is empty before each test
        self.collection.delete_many({})

    def tearDown(self):
        # Clean up any leftover data
        self.collection.delete_many({})

    def test_handle_options(self):
        response = self.client.options('/ClientReservation')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "CORS Preflight Succeeded"})
        self.assertEqual(response.headers['Access-Control-Allow-Origin'], 'http://localhost:3000')

    def test_reservation(self):
        reservation_data = {
            "name": "John Doe",
            "phone": "1234567890",
            "date": "2024-05-25",
            "time": "18:00",
            "status": "confirmed"
        }
        response = self.client.post(
            '/ClientReservation',
            data=json.dumps(reservation_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Reservation placed successfully"})

        # Verify that the data was inserted into the database
        reservation_in_db = self.collection.find_one({"ReservationName": "John Doe"})
        self.assertIsNotNone(reservation_in_db)
        self.assertEqual(reservation_in_db['ReservationPhone'], "1234567890")
        self.assertEqual(reservation_in_db['ReservationDate'], "2024-05-25")
        self.assertEqual(reservation_in_db['ReservationTime'], "18:00")
        self.assertEqual(reservation_in_db['ReservationStatus'], "confirmed")

if __name__ == '_main_':
    unittest.main()