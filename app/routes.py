#from flask_mysqldb import MySQL,MySQLdb  

from flask import Blueprint, render_template, request, redirect, url_for, session
from flask.json import jsonify
from flask.wrappers import Response

from app import app
from app import mysql
from flask_login import login_user, login_required, logout_user
#A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
#Axios doesnt work without this


#######################################################
##################''' Controllers '''##################
#######################################################
from app.src import User
from app.src import Chatbot
from app.src import Telecom
from app.src import Apis

#######################################################
##################''' Home '''##################
#######################################################
@app.route('/', methods=["GET", "POST"]) 
def home():
    if request.method == 'GET':
        return "Hello, You are in the XYRON Chatbot Application"
    else:
        return "Hello, You are in the XYRON Chatbot Application"

#######################################################
##################''' User Routes '''##################
#######################################################
## User registration
@app.route('/register', methods=["GET", "POST"]) 
def register():
    if request.method == 'GET':
        return request.get_json()['email']
    else:
        return User.register(mysql)

## User login using email and password
@app.route('/login', methods=["GET", "POST"]) 
def login():
    if request.method == 'POST':
        return User.login(mysql) 
    else:
        return jsonify(msg = "Login GET Request")

## User logout
@app.route('/logout')
@login_required
def logout():
    return User.logout()

## Check whether user is logged in
@app.route('/checkLogin', methods=["GET", "POST"]) 
def check():
    if request.method == 'GET':
        return User.checkLogin(mysql) 
    else:
        return ""

## View profile details
@app.route('/profile', methods=['GET','POST'])
def viewprofile():
    if request.method == 'GET':
        return User.viewprofile(mysql)
    if request.method == 'POST':
        return User.updateprofile(mysql)

@app.route('/password', methods=['POST'])
def password():
    return User.updatepassword(mysql)
# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.
@app.after_request
def refresh_expiring_jwts(response):
    return User.refresh(response)
#######################################################
################''' Telecom Routes '''#################
#######################################################

@app.route("/reply",methods=["GET","POST"])
def reply():
    if request.method == 'POST':
        # if request.get_json()['msg'] == "Hi":
        re = Chatbot.chat(request.get_json()['msg'])
        return {"reply" : re }


@app.route('/getPackageTypes', methods=["GET", "POST"]) 
def getPackageTypes():
    if request.method == 'POST':
        return Telecom.getPackageTypes(mysql)

@app.route('/getPackages', methods=["GET", "POST"]) 
def getPackages():
    if request.method == 'POST':
        return Telecom.getPackages(mysql)  
    
@app.route('/getPackage', methods=["GET", "POST"]) 
def getPackageInformation():
    if request.method == 'POST':
        return Telecom.getPackageInfo(mysql)

@app.route('/activateDataPackage', methods=["GET", "POST"]) 
def activateDataPackage():
    if request.method == 'POST':
        return Telecom.activateDataPackages(mysql)

@app.route('/getCurrentBalance', methods=["GET", "POST"]) 
def getCurrentBalance():
    if request.method == 'POST':
        return Telecom.getCurrentBalance(mysql)

@app.route('/sendEmail', methods=["GET", "POST"]) 
def sendEmail():
    if request.method == 'POST':
        return Telecom.sendEmail(mysql)

@app.route('/makeComplaint', methods=["GET", "POST"]) 
def makeComplaint():
    if request.method == 'POST':
        return Telecom.makeComplaint(mysql)

@app.route('/getUser', methods=["GET", "POST"]) 
def getUser():
    if request.method == 'POST':
        return Telecom.getUser(mysql)

@app.route('/getCryptoPrice', methods=["GET", "POST"]) 
def getCrypto():
    if request.method == 'POST':
        return Apis.getCrypto()
    
@app.route('/getCryptoPriceLKR', methods=["GET", "POST"]) 
def getCryptoLKR():
    if request.method == 'POST':
        return Apis.getCryptoLKR()

@app.route('/getMoneyValue', methods=["GET", "POST"]) 
def getMoneyValue():
    if request.method == 'POST':
        return Apis.getMoneyValue()

@app.route('/viewActivatedPackages', methods=["GET", "POST"]) 
def viewActivatedPackages():
    if request.method == 'POST':
        return Telecom.viewActivatedPackages(mysql)

@app.route('/viewActivatedPackagesByDate', methods=["GET", "POST"]) 
def viewActivatedPackagesByDate():
    if request.method == 'POST':
        return Telecom.viewActivatedPackagesByDate(mysql)


@app.route('/getFeedbacks', methods=["GET", "POST"]) 
def getFeedbacks():
    if request.method == 'GET':
        return Telecom.getFeedbacks(mysql)


@app.route("/sendFeedback",methods=["GET","POST"])
def sendFeedback():
    return Telecom.sendFeedback(mysql)