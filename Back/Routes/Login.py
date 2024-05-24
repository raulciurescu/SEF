from flask import Blueprint, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

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


client = MongoClient('localhost', 27017)
DB = client['FullAppSef']

Login_route = Blueprint('Login_route', __name__)

CORS(Login_route, origins='*', methods=['POST'], allow_headers=['Content-Type'], supports_credentials=True)

@Login_route.route('/Login', methods=['OPTIONS'])
def handle_options():
    response = jsonify({"message": "CORS Preflight Succeeded"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

@Login_route.route('/Login', methods=['POST'])
def Login():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('pwd')
        if DB.Manager.find_one({"ManagerEmail": email, "ManagerPassword": str(Encrypt(password))}) is not None:
            response = jsonify({"message": "Manager"})
            return response
        else:   
            staff = DB.Staff.find_one({"StaffEmail": email, "StaffPassword": str(Encrypt(password))})
            if staff:
                staff_id = staff.get('StaffID')
                response = jsonify({"message": "Staff", "staff_id": staff_id})
                return response
            else:
                response = jsonify({"message": "Invalid email or password"})
                return response

