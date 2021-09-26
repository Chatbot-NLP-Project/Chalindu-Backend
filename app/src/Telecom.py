from flask import request, session
from flask import jsonify
from flask_mysqldb import MySQL,MySQLdb
import re
import datetime
from datetime import (timedelta, timezone)


def getPackageTypes(mysql):
    type = request.get_json()['provider']
    print(type)
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT DISTINCT package_type FROM datapackage WHERE connection=%s",(type,))
    packageTypes = curl.fetchall()
    pt=[]
    curl.close()
    for i in range(0,len(packageTypes)):
        pt.append(packageTypes[i]['package_type'])
    return {
        "packageTypes" : pt
    }

def getPackages(mysql):
    type = request.get_json()['provider']
    packageType = request.get_json()['packageType']
    print(type)
    curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    curl.execute("SELECT DISTINCT name FROM datapackage WHERE connection=%s and package_type=%s",(type,packageType))
    packages = curl.fetchall()
    pckgs=[]
    curl.close()
    for i in range(0,len(packages)):
        pckgs.append(packages[i]['name'])
    return {
        "packageTypes" : pckgs
    }