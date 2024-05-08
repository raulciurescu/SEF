from flask import jsonify, request, Blueprint
from flask_cors import CORS
from MainCreateCollections import DB

manager_route = Blueprint('manager_route', __name__)

CORS(manager_route, origins='*', methods=['POST'], allow_headers=['Content-Type'], supports_credentials=True)



@manager_route.route('/ManagerRegister', methods=['POST'])
def ManagerRegister():
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
        try:
            DB.Manager.insert_one(manager)
            return jsonify({"message": "Manager added successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Method Not Allowed"}), 405
