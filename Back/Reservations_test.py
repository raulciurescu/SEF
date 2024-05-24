import unittest
from flask import Flask
from pymongo import MongoClient
from bson.objectid import ObjectId
import json

# Import the blueprint
from Routes.Reservations import Reservations_route

class ReservationsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Flask test client
        cls.app = Flask(__name__)
        cls.app.register_blueprint(Reservations_route)
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

    def test_get_reservations(self):
        # Insert a test reservation
        test_reservation = {
            "ReservationName": "Alice",
            "ReservationPhone": "9876543210",
            "ReservationDate": "2024-06-01",
            "ReservationTime": "20:00",
            "ReservationStatus": "Placed"
        }
        self.collection.insert_one(test_reservation)

        # Make a GET request to the /Reservations endpoint
        response = self.client.get('/Reservations')
        self.assertEqual(response.status_code, 200)

        # Verify the response data
        response_data = json.loads(response.data)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["ReservationName"], "Alice")
        self.assertEqual(response_data[0]["ReservationPhone"], "9876543210")
        self.assertEqual(response_data[0]["ReservationDate"], "2024-06-01")
        self.assertEqual(response_data[0]["ReservationTime"], "20:00")
        self.assertEqual(response_data[0]["ReservationStatus"], "Placed")

    def test_update_reservation(self):
        # Insert a test reservation
        test_reservation = {
            "ReservationName": "Bob",
            "ReservationPhone": "0123456789",
            "ReservationDate": "2024-07-01",
            "ReservationTime": "21:00",
            "ReservationStatus": "Placed"
        }
        reservation_id = self.collection.insert_one(test_reservation).inserted_id

        # Update the reservation status
        update_data = {"ReservationStatus": "Confirmed"}
        response = self.client.put(
            f'/Reservations/{reservation_id}',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Reservation Updated"})

        # Verify that the data was updated in the database
        updated_reservation = self.collection.find_one({"_id": reservation_id})
        self.assertIsNotNone(updated_reservation)
        self.assertEqual(updated_reservation["ReservationStatus"], "Confirmed")

if __name__ == '_main_':
    unittest.main()