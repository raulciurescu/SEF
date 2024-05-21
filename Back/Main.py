from flask import Flask
from Routes.Login import Login_route
from Routes.Staff import Staff_route
from Routes.Menu import Menu_route

app = Flask(__name__)

app.register_blueprint(Login_route)
app.register_blueprint(Staff_route)
app.register_blueprint(Menu_route)

if __name__ == '__main__':
    app.run(debug=True)