from flask import request, session
from flask import jsonify
from flask_mysqldb import MySQL,MySQLdb
import re
import datetime
from datetime import (timedelta, timezone)
from flask_mail import Mail, Message 
from app import mail
# def getCurrentBalance():
#     user_id = 


 
def getPackageTypes(mysql):
    type = request.get_json()['provider']
    print(type)
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT DISTINCT package_type FROM datapackage WHERE connection=%s",(type,))
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
    curl.execute("SELECT DISTINCT name FROM datapackage WHERE connection=%s and package_type=%s",(provider,packageType))
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
    curl.execute("SELECT * FROM datapackage WHERE connection=%s and package_type=%s and name=%s",(provider,packageType, packageName))
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
    curl.execute("SELECT * FROM datapackage WHERE connection=%s and name=%s",(provider, packageName))
    dataPackage = curl.fetchall()[0]
    fee = dataPackage['fee']
    anytime_data = dataPackage['anytime_data']
    night_time_data = dataPackage['night_time_data']
    g4_data = dataPackage['4g_data']
    curl.execute("SELECT * FROM user WHERE user_id=%s",(userID))
    user = curl.fetchone()
    
    balance = user['current_balance']
    new_anytime_data = float(anytime_data) + float(user['anytime_data'])
    new_night_time_data = float(night_time_data) + float(user['night_time_data'])
    new_4g_data = float(g4_data) + float(user['4g_data'])
    # print("user[anytime_data]")
    # print(user['anytime_data'])
    # print("anytime_data")
    # print(anytime_data)
    # print('night_time_data')
    # print(night_time_data)
    # print('user[night_time_data]')
    # print(user['night_time_data'])
    # print('user[anytime_data]')
    # print(user['anytime_data'])
    # print('g4_data')
    # print(g4_data)
    # print('user[4g_data]')
    # print(user['4g_data'])



    # float(balance)>= float(fee)
    if(float(balance)>= float(fee)):
        newBalance = float(balance)-float(fee)
        curl.execute("UPDATE user SET current_balance=%s, anytime_data=%s, night_time_data=%s, 4g_data=%s WHERE user_id=%s",(newBalance, new_anytime_data, new_night_time_data, new_4g_data, int(userID)))
        mysql.connection.commit()
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
    curl.execute("SELECT * FROM user WHERE user_id=%s",(userID))
    user = curl.fetchone()
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




