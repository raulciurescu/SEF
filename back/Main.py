# make the code see the CreateTheDataBase file
import sys
sys.path.append('d:\\SEF_2.0\\back\\DataBase\\CreateCollections')
sys.path.append('d:\\SEF_2.0\\back\\Routes\\ManagerRoute')
sys.path.append('d:\\SEF_2.0\\back\\Routes\\StaffRoute')
sys.path.append('d:\\SEF_2.0\\back\\Routes\\ClientRoute')
sys.path.append('d:\\Sef_2.0\\back\\Routes\\Login')
sys.path.append('d:\\SEF_2.0\\back\\QR')
sys.path.append('d:\\SEF_2.0\\back\\CreateApp')
sys.path.append('d:\\SEF_2.0\\back\\CriptareDecriptare')
from CriptareDecriptare import criptare_parola , decriptare_parola
from cryptography.fernet import Fernet
from MainCreateCollections import DB
from Routes.Login import Login_route
from QR import generate_qr_code
from CreateApp import app

#generate a key to use for the encryption
key = Fernet.generate_key()


generate_qr_code("https://www.google.com")

# Todo : remove Staff adding and Make a method to cript the password

DB.Manager.insert_one({"ManagerName" : "Teo" , "ManagerEmail": "teo@gmail.com" , "ManagerPassword": str(criptare_parola("teo",key))})
DB.Staff.insert_one({"StaffID" : "1" , "StaffName" : "Raul" , "StaffEmail": "raul@gmail.com" , "StaffPassword": str(criptare_parola("raul",key))})


app.register_blueprint(Login_route)



if __name__ == '__main__':
    app.run(debug=True)