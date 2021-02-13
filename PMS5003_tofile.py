import os
import sys
import serial
import datetime

date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M') #:%S
file_path = sys.argv[1]
port = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=60.0)


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

def empty(_filepath):
    return os.stat(_filepath).st_size == 0

def parsedData():
    data = getData(port)

    pm1 = data[10] * 256 + data[11]
    pm25 = data[12] * 256 + data[13]
    pm10 = data[14] * 256 + data[15]

    _pm1 = str(pm1)
    _pm25 = str(pm25)
    _pm10 = str(pm10)

    return '    { "date": "' + date + '", "pm1": "' + _pm1 + '", "pm25": "' + _pm25 + '", "pm10": "' + _pm10 + '" }\n'

def appendToFile():
    try:
        file = open(file_path, 'a+')

        if empty(file_path):
            file.write('{\n')
            file.write(parsedData())
            file.write('}')
        else:
            file.seek(file.tell() - 2, os.SEEK_SET)
            file.truncate()
            file.write(',\n')
            file.write(parsedData())
            file.write('}')

    except OSError:
        print('[' + date + '] Błąd przy zapisywaniu danych.')
        exit()

appendToFile()