from flask import jsonify, request, Blueprint
from flask_cors import CORS
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
DB = client['FullAppSef']

Reservations_route = Blueprint('Reservations_route', __name__)

CORS(Reservations_route, origins='*', methods=['GET','PUT'], allow_headers=['Content-Type'], supports_credentials=True)

@Reservations_route.route('/Reservations', methods=['GET'])
def Res():
    data = DB.Reservations.find({"ReservationStatus": "Placed"})
    data = [{"_id": str(doc["_id"]), "ReservationName": doc["ReservationName"], "ReservationPhone": doc["ReservationPhone"], "ReservationDate": doc["ReservationDate"], "ReservationTime": doc["ReservationTime"], "ReservationStatus": doc["ReservationStatus"]} for doc in data]
    return jsonify(data)

@Reservations_route.route('/Reservations/<id>', methods=['PUT'])
def update_reservation(id):
    data = request.get_json()
    DB.Reservations.update_one({"_id": ObjectId(id)}, {"$set": {"ReservationStatus": data["ReservationStatus"]}})
    return jsonify({"message": "Reservation Updated"})