import os
import sys
import serial
import datetime
import mysql.connector

date = datetime.datetime.now() #.strftime('%Y-%m-%d %H:%M') #:%S
port = serial.Serial(
    port = '/dev/ttyS0',
    baudrate = 9600,
    timeout = 60.0
)

database = mysql.connector.connect(
    host = "localhost",
    user = "mysql_admin",
    passwd = "as23qwCfG",
    database = "czujnik"
)

def getData(_port):
    data = b''
    while True:
        check1 = _port.read()
        if check1 == b'\x42':
            check2 = _port.read()
            if check2 == b'\x4d':
                data += check1 + check2
                data += _port.read(28)
                return data

data = getData(port)

pm1 = data[10] * 256 + data[11]
pm25 = data[12] * 256 + data[13]
pm10 = data[14] * 256 + data[15]

_pm1 = str(ord(pm1[256]))
_pm25 = str(ord(pm25[256]))
_pm10 = str(ord(pm10[256]))

cursor = database.cursor()

query = "INSERT INTO dane (date, pm1, pm25, pm10) VALUES (%s, %s, %s, %s)"
value = (date, _pm1, _pm25, _pm10)

cursor.execute(query, value)
database.commit()

database.close()
