from flask import request, session
from flask import jsonify
from flask_mysqldb import MySQL,MySQLdb
import re
import datetime
from datetime import (timedelta, timezone)
from flask_mail import Mail, Message 
from app import mail
import requests

# def getCurrentBalance():
#     user_id = 


 
def getPackageTypes(mysql):
    type = request.get_json()['provider']
    print(type)
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT DISTINCT package_type FROM DataPackage WHERE connection=%s",(type,))
    packageTypes = curl.fetchall()
    curl.close()
    for i in range(0, len(packageTypes)):
        packageTypes[i]["id"] = str(i)
    return jsonify(packageTypes = packageTypes)

def getPackages(mysql):
    provider = request.get_json()['provider']
    packageType = request.get_json()['packageType']
    print(type)
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT DISTINCT name FROM DataPackage WHERE connection=%s and package_type=%s",(provider,packageType))
    packages = curl.fetchall()
    curl.close()
    for i in range(0, len(packages)):
        packages[i]["id"] = str(i)
    return jsonify(packages = packages)

def getPackageInfo(mysql):
    provider = request.get_json()['provider']
    packageType = request.get_json()['packageType']
    packageName = request.get_json()['packageName']
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM DataPackage WHERE connection=%s and package_type=%s and name=%s",(provider,packageType, packageName))
    packageDetails = curl.fetchall()
    curl.close()

    return jsonify(
        packageDetails = packageDetails
    )

def activateDataPackages(mysql):
    provider = request.get_json()['provider']
    packageName = request.get_json()['packageName']
    userID = str(request.get_json()["userID"])
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM DataPackage WHERE connection=%s and name=%s",(provider, packageName))
    dataPackage = curl.fetchall()[0]
    fee = dataPackage['fee']
    print(dataPackage)
    packageID = int(dataPackage['data_package_id'])
    validityPeriod = int(dataPackage['validity_period'])
    activatedDate = datetime.datetime.now()
    anytime_data = dataPackage['anytime_data']
    night_time_data = dataPackage['night_time_data']
    g4_data = dataPackage['4g_data']
    curl.execute("SELECT * FROM User WHERE user_id=%s",(userID))
    user = curl.fetchone()
    
    balance = user['current_balance']
    new_anytime_data = float(anytime_data) + float(user['anytime_data'])
    new_night_time_data = float(night_time_data) + float(user['night_time_data'])
    new_4g_data = float(g4_data) + float(user['4g_data'])
    # print("user[anytime_data]")
    # print(user['anytime_data'])
    # float(balance)>= float(fee)
    if(float(balance)>= float(fee)):
        newBalance = float(balance)-float(fee)
        curl.execute("UPDATE User SET current_balance=%s, anytime_data=%s, night_time_data=%s, 4g_data=%s WHERE user_id=%s",(newBalance, new_anytime_data, new_night_time_data, new_4g_data, int(userID)))
        mysql.connection.commit()
        curl.execute("INSERT INTO ActivatedPackage (user_id, package_id, activated_date, expired) VALUES (%s,%s,%s,%s)",(userID, packageID, activatedDate, validityPeriod))
        mysql.connection.commit()
        curl.close()
        return jsonify(
            res = "Package is successfully activated"
        )
    else:
        return jsonify(
            res = "Your balance is not enough to activate the package"
        )


def getCurrentBalance(mysql):
    userID = str(request.get_json()["userID"])
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM User WHERE user_id=%s",(userID))
    user = curl.fetchone()
    curl.close()
    return jsonify( user = user)


def sendEmail(mysql):
    email = request.get_json()["email"]
    subject = request.get_json()["subject"]
    msg = request.get_json()['message']
    print(email)
    message = Message(subject, sender="xyronchatbot@gmail.com", recipients=[email])

    message.body = msg

    mail.send(message)

    return jsonify( res = "Email sent")

def makeComplaint(mysql):
    subject = request.get_json()["subject"]
    body = request.get_json()['body']
    userID = str(request.get_json()['userID'])
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM User WHERE user_id=%s",(userID))
    user = curl.fetchone()
    complainedDate = datetime.datetime.now() # The date of complaint
    email = str(user['email'])
    provider = str(user['sim_type'])
    phoneNumber = str(user['phone_number'])
    message = Message(subject, sender="xyronchatbot@gmail.com", recipients=["chalindumalshika2014@gmail.com"])
    message.html = "<p>User Email : "+ email + "</p>" +"<p>User Mobile Number : "+ phoneNumber+ "</p>" + "<h1>Complaint details, </h1>" + body
    mail.send(message)
    curl.execute("INSERT INTO Complaint (user_id, isp, subject, message, complain_date) VALUES (%s,%s,%s,%s,%s)",(userID, provider, subject, body, complainedDate))
    mysql.connection.commit()
    curl.close()
    return jsonify( res = "Complaint is sent to the " + provider + " customer care center")

def viewComplaint(mysql):
    userID = str(request.get_json()['userID'])
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM Complaint WHERE user_id=%s",(userID))
    complaints = curl.fetchall()
    curl.close()
    Null = 0
    if (not complaints):
        Null = 1
        complaints = []
    return jsonify( complaints = complaints, Null = Null)

def getUser(mysql):
    userID = str(request.get_json()['userID'])
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM User WHERE user_id=%s",(userID))
    user = curl.fetchone()
    return jsonify( user = user)

def viewActivatedPackages(mysql):
    userID = str(request.get_json()['userID'])
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM ActivatedPackage NATURAL JOIN DataPackage WHERE DataPackage.data_package_id = ActivatedPackage.package_id AND user_id=%s",(userID))
    activatedPackages = curl.fetchall()
    Null = 0
    if (not activatedPackages):
        Null = 1
    print(activatedPackages)
    return jsonify( activatedPackages = activatedPackages, Null = Null)

def viewActivatedPackagesByDate(mysql):
    userID = str(request.get_json()['userID'])
    date = str(request.get_json()['date'])
    date = date + "%"
    print(date)
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM ActivatedPackage NATURAL JOIN DataPackage WHERE DataPackage.data_package_id = ActivatedPackage.package_id AND user_id=%s AND ActivatedPackage.activated_date LIKE %s" ,(userID, date))
    activatedPackages = curl.fetchall()
    Null = 0
    if (not activatedPackages):
        Null = 1
    # print(activatedPackages)
    return jsonify( activatedPackages = activatedPackages, Null = Null)


def getFeedbacks(mysql):
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT * FROM Feedback ")
    feedbacks = curl.fetchall()
    Null = 0
    if (not feedbacks):
        Null = 1
        feedbacks = []
    return jsonify( feedbacks = feedbacks, Null = Null)

def sendFeedback(mysql):
    feedback = request.get_json()['feedback']
    userID = request.get_json()['userID']
    rating = str(request.get_json()['rating'])
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('INSERT INTO Feedback (user_id, chatbot_type, rating, feedback) VALUES (%s,%s,%s,%s)', (userID, "Telecommunication", rating, feedback))
    mysql.connection.commit()
    return "successful"

def getNumberOfUsers(mysql):
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT COUNT(*) AS users FROM User")
    numberOfUsers = int(curl.fetchone()['users']) - 1
    return jsonify (numberOfUsers = numberOfUsers)