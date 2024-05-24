from flask import jsonify, request, Blueprint
from flask_cors import CORS
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
DB = client['FullAppSef']

Orders_route = Blueprint('Orders_route', __name__)

CORS(Orders_route, origins='*', methods=['POST','GET', 'DELETE', 'PUT'], allow_headers=['Content-Type'], supports_credentials=True)

@Orders_route.route('/Orders', methods=['OPTIONS'])
def handle_options():
    response = jsonify({"message": "CORS Preflight Succeeded"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

@Orders_route.route('/Orders', methods=['GET' ])
def Orders():
    if request.method == 'GET':
        data = DB.Orders.find({"OrderStatus": "Placed"})
        data = [{"_id": str(doc["_id"]), "StaffID": doc["StaffID"],"OrderID": doc["OrderID"],  "OrderProducts": doc["OrederProducts"], "OrderStatus": doc["OrderStatus"],"OrderPrice": doc["OrderPrice"]} for doc in data]
        return jsonify(data)

@Orders_route.route('/Orders/<string:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        order_data = request.get_json()
        DB.Orders.update_one(
            {"OrderID": order_id},
            {"$set": {"OrderStatus": order_data.get("OrderStatus")}}
        )
        return jsonify({"message": "Order updated"})
    except Exception as e:
        return jsonify({"error": str(e)})