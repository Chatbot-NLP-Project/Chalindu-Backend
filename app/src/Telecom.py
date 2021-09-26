from flask import request, session
from flask import jsonify
from flask_mysqldb import MySQL,MySQLdb
import re
import datetime
from datetime import (timedelta, timezone)


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
    userID = request.get_json()["userID"]
    packageFee = request.get_json()["packageFee"]
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT fee FROM datapackage WHERE connection=%s and name=%s",(provider, packageName))
    fee = curl.fetchall()
    curl.execute("SELECT current_balance FROM user WHERE user_id=%s",(userID))
    balance = curl.fetchone()
    # float(balance)>= float(fee[0])
    if(float(balance["current_balance"])>= float(fee[0]["fee"])):
        newBalance = float(balance["current_balance"])-float(fee[0]["fee"])
        curl.execute("UPDATE user SET current_balance=%s WHERE user_id=%s",(newBalance, int(userID)))
        mysql.connection.commit()
        return jsonify(
            res = "Package is successfully activated"
        )
    else:
        return jsonify(
            res = "Your balance is not enough to activate the package"
        )
