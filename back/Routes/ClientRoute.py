from flask import jsonify, request, Blueprint
from flask_cors import CORS
from MainCreateCollections import DB

client_route = Blueprint('client_route', __name__)

CORS(client_route, origins='*', methods=['POST','GET','DELETE','PUT'], allow_headers=['Content-Type'], supports_credentials=True)

# For the "ClientMenu" page to get the menu 
# The client can see the menu and choose the items he wants to order
# The client can see the price of each item
# The client can see the description of each item
# The client can see the category of each item
# also after the client choose the items he wants to order he can click on the "Order" button
# the order will be automatically sent in the "Orders" collection
# the client can see the order status
# the client can see the order number
# the client can see the total price of the order
# the client can see the time of the order
# the client can see the date of the order
# the client can see the order items
# the client can see the order items price
# the client can see the order items quantity
# the client can see the order items total price

@client_route.route('/ClientMenu', methods=['GET'])
def ClientMenu():
    if request.method == 'GET':
        try:
            menu = list(DB.Menu.find())
            return jsonify({"menu": menu}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Method Not Allowed"}), 405

# For the "ClientOrders" page to get the orders
# The client can see the order status
