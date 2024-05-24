import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from Routes.Orders import Orders_route

class TestOrdersRoute(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(Orders_route)
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_orders(self):
        # Mocking the database find method
        with patch('pymongo.collection.Collection.find') as mock_find:
            # Simulate finding orders with "Placed" status
            mock_find.return_value = [
                {"_id": "1", "StaffID": "123", "OrderID": "456", "OrederProducts": "Product A, Product B", "OrderStatus": "Placed", "OrderPrice": 10.00},
                {"_id": "2", "StaffID": "456", "OrderID": "789", "OrederProducts": "Product C", "OrderStatus": "Placed", "OrderPrice": 5.00}
            ]

            # Make a GET request to retrieve orders with "Placed" status
            response = self.app.get('/Orders')

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 2)
            self.assertEqual(response.json[0]["StaffID"], "123")
            self.assertEqual(response.json[0]["OrderID"], "456")
            self.assertEqual(response.json[1]["StaffID"], "456")
            self.assertEqual(response.json[1]["OrderID"], "789")

    def test_update_order(self):
        # Mocking the database update_one method
        with patch('pymongo.collection.Collection.update_one') as mock_update_one:
            # Simulate a successful update
            mock_update_one.return_value = True

            # Make a PUT request to update an order
            response = self.app.put('/Orders/456', json={"OrderStatus": "Completed"})

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], "Order updated")

if __name__ == "__main__":
    unittest.main()
