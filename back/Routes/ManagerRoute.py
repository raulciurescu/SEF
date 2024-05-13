from flask import jsonify, request, Blueprint
from flask_cors import CORS
from MainCreateCollections import DB



manager_route = Blueprint('manager_route', __name__)

CORS(manager_route, origins='*', methods=['POST','GET','DELETE','PUT'], allow_headers=['Content-Type'], supports_credentials=True)



# For manager to check if there is a manager in the database
# If there is no manager in the database, the manager can add a manager
# If there is a manager neet to get a mesage that there is a manager in the database

@manager_route.route('/ManagerRegister', methods=['POST'])
def Manager():
    if request.method == 'POST':
        data = request.json
        manager_name = data.get('name')
        manager_email = data.get('email')
        manager_password = data.get('pwd')
        manager = {
            "ManagerName": manager_name,
            "ManagerEmail": manager_email,
            "ManagerPassword": manager_password
        }
        if DB.Manager.find_one() is None:
            DB.Manager.insert_one(manager)
            return jsonify({"message": "Manager added successfully"}), 201
        elif DB.Manager.find_one() is not None:
            return jsonify({"message": "Manager already exists"}), 200
    else:
        return jsonify({"error": "Method Not Allowed"}), 405  
    
# For the manager to login

@manager_route.route('/ManagerLogin', methods=['POST'])
def ManagerLogin():
    if request.method == 'POST':
        data = request.json
       
    
# For the manager to add a staff or multiple staffs also to view all staffs or delete a staff or multiple staffs

@manager_route.route('/ManagerStaff', methods=['POST', 'GET', 'DELETE'])
def ManagerStaff():
    if request.method == 'POST':
        data = request.json
        staff_name = data.get('name')
        staff_email = data.get('email')
        staff_password = data.get('pwd')
        staff = {
            "StaffName": staff_name,
            "StaffEmail": staff_email,
            "StaffPassword": staff_password
        }
        try:
            DB.Staff.insert_one(staff)
            return jsonify({"message": "Staff added successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == 'GET':
        try:
            staffs = list(DB.Staff.find())
            return jsonify(staffs), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == 'DELETE':
        data = request.json
        staff_email = data.get('email')
        try:
            DB.Staff.delete_one({"StaffEmail": staff_email})
            return jsonify({"message": "Staff deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Method Not Allowed"}), 405
    
# For the manager to add a product or multiple products also to view all products or delete a product or multiple products or to update a product

@manager_route.route('/ManagerProduct', methods=['POST', 'GET', 'DELETE', 'PUT'])
def ManagerProduct():
    if request.method == 'POST':
        data = request.json
        product_name = data.get('name')
        product_price = data.get('price')
        product_quantity = data.get('quantity')
        product = {
            "ProductName": product_name,
            "ProductPrice": product_price,
            "ProductQuantity": product_quantity
        }
        try:
            DB.Product.insert_one(product)
            return jsonify({"message": "Product added successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == 'GET':
        try:
            products = list(DB.Product.find())
            return jsonify(products), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == 'DELETE':
        data = request.json
        product_name = data.get('name')
        try:
            DB.Product.delete_one({"ProductName": product_name})
            return jsonify({"message": "Product deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == 'PUT':
        data = request.json
        product_name = data.get('name')
        product_price = data.get('price')
        product_quantity = data.get('quantity')
        try:
            DB.Product.update_one({"ProductName": product_name}, {"$set": {"ProductPrice": product_price, "ProductQuantity": product_quantity}})
            return jsonify({"message": "Product updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Method Not Allowed"}), 405