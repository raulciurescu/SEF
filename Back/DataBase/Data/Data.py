table_Manager = {
    "ManagerName": {"type": "string"},
    "ManagerEmail": {"type": "string"},
    "ManagerPassword": {"type": "string"},
}

table_Staff = {
    "StaffID": {"type": "string"},
    "StaffName": {"type": "string"},
    "StaffEmail": {"type": "string"},
    "StaffPassword": {"type": "string"},
}

table_Menu = {
    "Category": {"type": "string"},
    "ProductName": {"type": "string"},
    "Description": {"type": "string"},
    "Price": {"type": "string"},
}

table_Orders = {
    "StaffID": {"type": "string"}, 
    "OrderID": {"type": "string"},
    "OrderProducts": {"type": "string"}, 
    "OrderStatus": {"type" : "string"}, 
    "OrderPrice": {"type": "string"},
}

table_Reservations = {
    "ReservationName": {"type": "string"},
    "ReservationPhone": {"type": "string"},
    "ReservationDate": {"type": "string"},
    "ReservationTime": {"type": "string"},
    "ReservationStatus": {"type" : "string"}, 
}