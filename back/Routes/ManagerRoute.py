from flask import jsonify, request, Blueprint
from flask_cors import CORS
from MainCreateCollections import DB
from CriptareDecriptare import criptare_parola

manager_route = Blueprint('manager_route', __name__)

CORS(manager_route, origins='*', methods=['POST','GET','DELETE','PUT'], allow_headers=['Content-Type'], supports_credentials=True)

# For Manage the Staff 
@manager_route.route('/Staff', methods=['POST','GET','DELETE','PUT'])
def Staff():
    if request.method == 'POST':
        data = request.json
        id = data.get('id')
        name = data.get('name')
        email = data.get('email')
        password = data.get('pwd')
        DB.Staff.insert_one({"StaffID": id, "StaffName": name, "StaffEmail": email, "StaffPassword": str(criptare_parola(password))})
    if request.method == 'GET':
        staff = DB.Staff.find()
        return jsonify(list(staff))
