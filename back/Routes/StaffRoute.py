from flask import jsonify, request, Blueprint
from flask_cors import CORS
from MainCreateCollections import DB

staff_route = Blueprint('staff_route', __name__)

CORS(staff_route, origins='*', methods=['POST','GET','DELETE','PUT'], allow_headers=['Content-Type'], supports_credentials=True)


# For the staff to login



    
