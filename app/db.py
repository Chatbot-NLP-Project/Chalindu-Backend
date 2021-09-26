from app import app
from os import environ as env
from flask_mysqldb import MySQL
from datetime import timedelta
# app = Flask(__name__)
 

app.config['MYSQL_HOST'] = env.get('DB_HOST')
app.config['MYSQL_USER'] = env.get('DB_USER')
app.config['MYSQL_PASSWORD'] = env.get('DB_PASSWORD')
app.config['MYSQL_DB'] = env.get('DB_NAME')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.config["JWT_SECRET_KEY"] = env.get('SECRET_KEY') 
app.config["JWT_COOKIE_SECURE"] = True
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)