from flask import jsonify, request, Blueprint
from flask_cors import CORS
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
DB = client['FullAppSef']

Menu_route = Blueprint('Menu_route', __name__)

CORS(Menu_route, origins='*', methods=['POST','GET', 'DELETE'], allow_headers=['Content-Type'], supports_credentials=True)

@Menu_route.route('/Menu', methods=['POST','GET'])
def Menu():
    if request.method == 'POST':
        data = request.json
        category = data.get('Category')
        product_name = data.get('ProductName')
        description = data.get('Description')
        price = data.get('Price')
        DB.Menu.insert_one({"Category": category, "ProductName": product_name, "Description": description, "Price": price})
        return jsonify({"message": "Product added"}), 200
    elif request.method == 'GET':
        data = DB.Menu.find()
        # Convert ObjectId to string before returning JSON
        data = [{"_id": str(doc["_id"]), "Category": doc["Category"], "ProductName": doc["ProductName"], "Description": doc["Description"], "Price": doc["Price"]} for doc in data]
        return jsonify(data)

#delete method for object with specific id
@Menu_route.route('/Menu1/<string:_id>', methods=['DELETE'])
def delete_Menu(_id):
    try:
        DB.Menu.delete_one({"_id": ObjectId(_id)})
        return jsonify({"message": "Menu deleted"})
    except Exception as e:
        return jsonify({"error": str(e)})