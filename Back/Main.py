from flask import Flask
from Routes.Login import Login_route
from Routes.Staff import Staff_route
from Routes.Menu import Menu_route
from Routes.Orders import Orders_route
from QR.QR import generate_qr_code 
from Routes.Reservations import Reservations_route
from Routes.PlaceOrder import PlaceOrders_route
app = Flask(__name__)

app.register_blueprint(Login_route)
app.register_blueprint(Staff_route)
app.register_blueprint(Menu_route)
app.register_blueprint(Orders_route)
app.register_blueprint(Reservations_route)
app.register_blueprint(PlaceOrders_route)

if __name__ == '__main__':
    app.run(debug=True)