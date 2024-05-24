from flask import jsonify, request, Blueprint
from flask_cors import CORS
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
DB = client['FullAppSef']

PlaceOrders_route = Blueprint('PlaceOrders_route', __name__)

CORS(PlaceOrders_route, origins='*', methods=['POST'], allow_headers=['Content-Type'], supports_credentials=True)

@PlaceOrders_route.route('/table_Orders', methods=['OPTIONS'])
def handle_options():
    response = jsonify({"message": "CORS Preflight Succeeded"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

@PlaceOrders_route.route('/table_Orders', methods=['POST' ])
def MakeOrders():
    data = request.json
    StaffID = data.get('StaffID')
    OrderID = data.get('OrderID')
    OrederProducts = data.get('OrederProducts')
    OrderStatus = data.get('OrderStatus')
    OrderPrice = data.get('OrderPrice')
    DB.Orders.insert_one({"StaffID": StaffID, "OrderID": OrderID, "OrederProducts": OrederProducts, "OrderStatus": OrderStatus, "OrderPrice": OrderPrice})
    return jsonify({"message": "Order made"}), 200
    
