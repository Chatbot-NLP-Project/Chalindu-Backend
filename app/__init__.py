#app.py /request-grab data
#pip install python-dotenv
#pip install flask-mysqldb
#pip install bcrypt
#pip install -U flask-cors
#pip install flask-login
#pip install jwtew

from flask import Flask
from flask_mysqldb import MySQL
from os import environ as env
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_cors import CORS, cross_origin

app = Flask(__name__)
mysql = MySQL(app)
CORS(app)
jwt = JWTManager(app)
login_manager = LoginManager()
login_manager.init_app(app)

# app.secret_key = env.get('SECRET_KEY')

from app import routes
from app import db
