# Encrypt the message
def Encrypt(s ):
    n = 3
    binary_str = ''.join(format(ord(c), '08b') for c in s)
    
    # Shift the binary string to the left by n positions
    shifted_binary_str = binary_str[n:] + '0' * n
    
    # Convert the shifted binary string back to a string
    shifted_str = ''.join(chr(int(shifted_binary_str[i:i+8], 2)) for i in range(0, len(shifted_binary_str), 8))
    
    return shifted_str



# Decrypt the message
def Decrypt(s ):
    n = 3
    # Convert the string to its binary representation
    binary_str = ''.join(format(ord(c), '08b') for c in s)
    
    # Shift the binary string to the right by n positions
    shifted_binary_str = '0' * n + binary_str[:-n]
    
    # Convert the shifted binary string back to a string
    shifted_str = ''.join(chr(int(shifted_binary_str[i:i+8], 2)) for i in range(0, len(shifted_binary_str), 8))
    
    return shifted_str


from flask import jsonify, request, Blueprint
from flask_cors import CORS
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
DB = client['FullAppSef']

Staff_route = Blueprint('Staff_route', __name__)

CORS(Staff_route, origins='*', methods=['POST','GET', 'DELETE'], allow_headers=['Content-Type'], supports_credentials=True)

@Staff_route.route('/Staff', methods=['OPTIONS'])
def handle_options():
    response = jsonify({"message": "CORS Preflight Succeeded"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

@Staff_route.route('/Staff', methods=['POST','GET' ])
def Staff():
    if request.method == 'POST':
        data = request.get_json()
        StaffID = data.get('StaffID')
        StaffName = data.get('StaffName')
        StaffEmail = data.get('StaffEmail')
        StaffPassword = data.get('StaffPassword')
        DB.Staff.insert_one({"StaffID": StaffID, "StaffName": StaffName, "StaffEmail": StaffEmail, "StaffPassword": str(Encrypt(StaffPassword))})
        return jsonify({"message": "Staff added"})
    elif request.method == 'GET':
        data = DB.Staff.find()
        # Convert ObjectId to string before returning JSON
        data = [{"_id": str(doc["_id"]), "StaffID": doc["StaffID"], "StaffName": doc["StaffName"], "StaffEmail": doc["StaffEmail"], "StaffPassword": str(Decrypt(doc["StaffPassword"]))} for doc in data]
        return jsonify(data)
   
@Staff_route.route('/Staff1/<string:StaffID>', methods=['DELETE'])
def delete_Staff(StaffID):
    try:
        DB.Staff.delete_one({"StaffID": StaffID})
        return jsonify({"message": "Staff deleted"})
    except Exception as e:
        return jsonify({"error": str(e)})