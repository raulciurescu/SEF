from flask import Blueprint, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
DB = client['FullAppSef']

ClientReservation_route = Blueprint('ClientReservation_route', __name__)

# Allow requests from the React frontend
CORS(ClientReservation_route, origins='http://localhost:3000', methods=['POST'], allow_headers=['Content-Type'], supports_credentials=True)

@ClientReservation_route.route('/ClientReservation', methods=['OPTIONS'])
def handle_options():
    response = jsonify({"message": "CORS Preflight Succeeded"})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response

@ClientReservation_route.route('/ClientReservation', methods=['POST'])
def Reservation():
    if request.method == 'POST':
        data = request.json
        ReservationName = data.get('name')
        ReservationPhone = data.get('phone')
        ReservationDate = data.get('date')
        ReservationTime = data.get('time')
        ReservationStatus = data.get('status')
        DB.Reservations.insert_one({"ReservationName": ReservationName, "ReservationPhone": ReservationPhone, "ReservationDate": ReservationDate, "ReservationTime": ReservationTime, "ReservationStatus": ReservationStatus})
        response = jsonify({"message": "Reservation placed successfully"})
        return response

@ClientReservation_route.route('/ClientReservation', methods=['GET'])
def GetReservations():
    if request.method == 'GET':
        Reservations = list(DB.Reservations.find())
        response = jsonify(Reservations)
        return response