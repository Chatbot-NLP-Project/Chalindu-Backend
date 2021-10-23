#app.py /request-grab data
#pip install python-dotenv
#pip install flask-mysqldb
#pip install bcrypt
#pip install -U flask-cors
#pip install flask-login
#pip install jwtew
#pip install Flask-Mail

from flask import Flask
from flask_mysqldb import MySQL
from os import environ as env
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message 
from datetime import timedelta


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "Xyronchatbot@gmail.com"
app.config['MAIL_PASSWORD'] = "Xyron2021"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config["JWT_SECRET_KEY"] = env.get('SECRET_KEY') 
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)
app.config["JWT_COOKIE_CSRF_PROTECT"] = True 
app.config["JWT_ACCESS_CSRF_HEADER_NAME"] = "X-CSRF-TOKEN-ACCESS"
app.config["JWT_REFRESH_CSRF_HEADER_NAME"] = "X-CSRF-TOKEN-REFRESH"

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'Dq0BIKNmDo'
app.config['MYSQL_PASSWORD'] = 'BkAuvPMTov'
app.config['MYSQL_DB'] = 'Dq0BIKNmDo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

CORS(app)
jwt = JWTManager(app)
login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)

from app import routes
from app import db


# app.secret_key = env.get('SECRET_KEY')
