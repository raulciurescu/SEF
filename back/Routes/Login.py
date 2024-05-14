from flask import jsonify, request, Blueprint
from flask_cors import CORS
from MainCreateCollections import DB
from CriptareDecriptare import decriptare_parola

Login_route = Blueprint('Login_route', __name__)

CORS(Login_route, origins='*', methods=['POST'], allow_headers=['Content-Type'], supports_credentials=True)

@Login_route.route('/Login', methods=['POST'])
def Login():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('pwd')
        if DB.Manager.find_one({"ManagerEmail": email, "ManagerPassword": str(decriptare_parola(password))}) is not None:
            return jsonify({"message": "Manager"}), 200
        elif DB.Staff.find_one({"StaffEmail": email, "StaffPassword": str(decriptare_parola(password))}) is not None:
            return jsonify({"message": "Staff"}), 200