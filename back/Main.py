# make the code see the CreateTheDataBase file
import sys
sys.path.append('d:\\SEF_2.0\\back\\DataBase\\CreateCollections')
from MainCreateCollections import DB
from ManagerRoute import manager_route
from CreateApp import app

app.register_blueprint(manager_route)

if __name__ == '__main__':
    app.run(debug=True)