from flask import jsonify, request, Blueprint
from flask_cors import CORS
from MainCreateCollections import DB

staff_route = Blueprint('staff_route', __name__)

CORS(staff_route, origins='*', methods=['POST','GET','DELETE','PUT'], allow_headers=['Content-Type'], supports_credentials=True)


# For the staff to login

@staff_route.route('/StaffLogin', methods=['POST'])
def StaffLogin():
    if request.method == 'POST':
        data = request.json
        staff_email = data.get('email')
        staff_password = data.get('pwd')
        try:
            staff = DB.Staff.find_one({"StaffEmail": staff_email})
            if staff:
                if staff_password == staff["StaffPassword"]:
                    return jsonify({"message": "Login successful"}), 200
                else:
                    return jsonify({"error": "Invalid password"}), 401
            else:
                return jsonify({"error": "Staff not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Method Not Allowed"}), 405
    

    
