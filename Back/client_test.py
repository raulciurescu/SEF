import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from Routes.Client import Client_route

class TestClientRoute(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(Client_route)
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_place_order(self):
        # Mocking the database insert_one method
        with patch('pymongo.collection.Collection.insert_one') as mock_insert_one:
            # Simulate a successful insertion
            mock_insert_one.return_value = True

            # Make a POST request to place an order
            response = self.app.post('/Client', json={
                "id": "123",
                "items": ["Product A", "Product B"],
                "status": "Pending",
                "price": 15.00
            })

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], "Order placed successfully")


    def test_get_menu(self):
        # Mocking the database find method
        with patch('pymongo.collection.Collection.find') as mock_find:
            # Simulate retrieving menu items
            mock_find.return_value = [
                {"Category": "Beverages", "ProductName": "Coffee", "Description": "Freshly brewed coffee", "Price": 2.50},
                {"Category": "Beverages", "ProductName": "Tea", "Description": "Assorted tea varieties", "Price": 2.00},
                {"Category": "Desserts", "ProductName": "Cake", "Description": "Delicious cake slices", "Price": 3.00}
            ]

            # Make a GET request to retrieve menu items
            response = self.app.get('/Client')

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 3)
            self.assertEqual(response.json[0]["Category"], "Beverages")
            self.assertEqual(response.json[1]["ProductName"], "Tea")
            self.assertEqual(response.json[2]["Price"], 3.00)

if __name__ == "__main__":
    unittest.main()
