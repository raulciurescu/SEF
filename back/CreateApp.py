from flask import Flask
from flask_cors import CORS


app = Flask(__name__,static_folder='d:\\FULL_SEF_APP\\build')

CORS(app, supports_credentials=True)