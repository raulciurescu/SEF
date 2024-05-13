# make the code see the CreateTheDataBase file
import sys
sys.path.append('d:\\SEF_2.0\\back\\DataBase\\CreateCollections')
sys.path.append('d:\\SEF_2.0\\back\\Routes\\ManagerRoute')
sys.path.append('d:\\SEF_2.0\\back\\Routes\\StaffRoute')
sys.path.append('d:\\SEF_2.0\\back\\Routes\\ClientRoute')
sys.path.append('d:\\Sef_2.0\\back\\Routes\\Login')
from MainCreateCollections import DB
from Routes.Login import Login_route
from QR import generate_qr_code
from CreateApp import app

generate_qr_code("https://www.google.com")

# Todo : remove Staff adding and Make a method to cript the password

DB.Manager.insert_one({"ManagerName" : "Teo" , "ManagerEmail": "teo@gmail.com" , "ManagerPassword": "teo"})
DB.Staff.insert_one({"StaffID" : "1" , "StaffName" : "Raul" , "StaffEmail": "raul@gmail.com" , "StaffPassword": "raul"})


app.register_blueprint(Login_route)



if __name__ == '__main__':
    app.run(debug=True)