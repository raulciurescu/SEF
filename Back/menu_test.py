import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from Routes.Menu import Menu_route

class TestMenuRoute(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.register_blueprint(Menu_route)
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_add_product(self):
        # Mocking the database insert_one method
        with patch('pymongo.collection.Collection.insert_one') as mock_insert_one:
            # Simulate a successful insertion
            mock_insert_one.return_value = True

            # Make a POST request to add a new product
            response = self.app.post('/Menu', json={
                "Category": "Beverages",
                "ProductName": "Coffee",
                "Description": "Freshly brewed coffee",
                "Price": 2.50
            })

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], "Product added")

    def test_get_menu(self):
        # Mocking the database find method
        with patch('pymongo.collection.Collection.find') as mock_find:
            # Simulate finding products
            mock_find.return_value = [
                {"_id": "1", "Category": "Beverages", "ProductName": "Coffee", "Description": "Freshly brewed coffee", "Price": 2.50}
            ]

            # Make a GET request to retrieve the menu
            response = self.app.get('/Menu')

            # Assert the response
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 1)
            self.assertEqual(response.json[0]["Category"], "Beverages")
            self.assertEqual(response.json[0]["ProductName"], "Coffee")

    def test_delete_menu(self):
        # Mocking the database delete_one method
        with patch('pymongo.collection.Collection.delete_one') as mock_delete_one:
            # Simulate a successful deletion
            mock_delete_one.return_value = True

            # Make a DELETE request to delete a product
            response = self.app.delete('/Menu1/1')

            # Assert the response
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
