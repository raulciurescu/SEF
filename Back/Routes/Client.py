from flask import Blueprint, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
DB = client['FullAppSef']

Client_route = Blueprint('Client_route', __name__)

CORS(Client_route, origins='*', methods=['POST'], allow_headers=['Content-Type'], supports_credentials=True)

@Client_route.route('/Client', methods=['OPTIONS'])
def handle_options():
    response = jsonify({"message": "CORS Preflight Succeeded"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

@Client_route.route('/Client', methods=['POST','GET'])
def Client():
    if request.method == 'POST':
        data = request.json
        StaffID = 0
        Order_ID = data.get('id')
        Order_Products = data.get('items')
        Order_Status = data.get('status')
        Order_Price = data.get('price')
        DB.Orders.insert_one({"StaffID": StaffID, "OrderID": Order_ID, "OrderProducts": Order_Products, "OrderStatus": Order_Status, "OrderPrice": Order_Price})
        response = jsonify({"message": "Order placed successfully"})
        return response.message
    if request.method == 'GET':
        menu_items = list(DB.Menu.find({}, {"_id": 0}))  # Retrieve menu items from the database
        return jsonify(menu_items)