import unittest
from flask import Flask
from pymongo import MongoClient
import json

# Import the blueprint
from Routes.PlaceOrder import PlaceOrders_route  # Update to the actual module name

class PlaceOrdersTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the Flask test client
        cls.app = Flask(__name__)
        cls.app.register_blueprint(PlaceOrders_route)
        cls.client = cls.app.test_client()

        # Set up the test database connection
        cls.client_db = MongoClient('localhost', 27017)
        cls.db = cls.client_db['FullAppSef']
        cls.collection = cls.db['Orders']

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
        response = self.client.options('/table_Orders')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "CORS Preflight Succeeded"})
        self.assertEqual(response.headers['Access-Control-Allow-Origin'], '*')

    def test_make_orders(self):
        order_data = {
            "StaffID": "staff123",
            "OrderID": "order456",
            "OrederProducts": ["product1", "product2"],  # Use the correct field name
            "OrderStatus": "",
            "OrderPrice": 100.0
        }
        response = self.client.post(
            '/table_Orders',
            data=json.dumps(order_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Order made"})

        # Verify that the data was inserted into the database
        order_in_db = self.collection.find_one({"OrderID": "order456"})
        self.assertIsNotNone(order_in_db)
        self.assertEqual(order_in_db['StaffID'], "staff123")
        self.assertEqual(order_in_db['OrederProducts'], ["product1", "product2"])  # Correct field name
        self.assertEqual(order_in_db['OrderStatus'], "pending")
        self.assertEqual(order_in_db['OrderPrice'], "100.0")  # Ensure this is stored as a string

if __name__ == '_main_':
    unittest.main()