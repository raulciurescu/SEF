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

from pymongo import MongoClient
db = MongoClient("mongodb://localhost:27017/")
DB = db["FullAppSef"]

def AddAManager():
    DB.Manager.insert_one({"ManagerName" : "Teo" , "ManagerEmail" : "teo@gmail.com" , "ManagerPassword" : Encrypt("teo")})
    DB.Staff.insert_one({"StaffID" : "1" , "StaffName" : "Raul" , "StaffEmail" : "raul@gmail.com" , "StaffPassword" : Encrypt("raul")})
    DB.Orders.insert_one({"StaffID" : "" , "OrderID" : "1" , "OrederProducts" : "paste pizza", "OrderStatus" : "Placed", "OrderPrice" : "2000"})
    DB.Orders.insert_one({"StaffID" : "" , "OrderID" : "2" , "OrederProducts" : "pene", "OrderStatus" : "Placed", "OrderPrice" : "20"})
    DB.Reservations.insert_one({"ReservationName" : "Raul" , "ReservationPhone" : "0722222222" , "ReservationDate" : "2021-06-01", "ReservationTime" : "12:00", "ReservationStatus" : "Placed"})
    DB.Reservations.insert_one({"ReservationName" : "Teo" , "ReservationPhone" : "0722222222" , "ReservationDate" : "2021-06-01", "ReservationTime" : "12:00", "ReservationStatus" : "Placed"})



# THAT IS IN CASE YOU NEED TO ADD A MANAGER TO THE DATABASE

