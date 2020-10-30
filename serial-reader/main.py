import sys
import time

from serialWrapper import SerialWrapper
from dataFunctions import dataFunctions
import database as db

SEPARATOR = [0x0A, 0x0D]
BAUD = 11520

#init database
dbClient = db.initDB()

#init serial wrapper
ser = SerialWrapper()
e = ser.openSerial(BAUD)

if e:
    print("could not open serial connection")
    print("The microcontroller needs to be reset after every run. Try unplugging it.")
    sys.exit()

#keep track of current time gathered from telemetry
flightTime = 0
engineTime = 0
while True:
    #test for frame separator, read one byte at a time so it aligns itself
    if not (ser.readBytes(1) == SEPARATOR[0] and ser.readBytes(1) == SEPARATOR[1]):
        print("failed")
        continue

    frameId = ser.readBytes(1)
    data = dataFunctions[frameId](ser)

    #handle flight controller data
    if data[0].source == "flight":
        #update time
        if data[0].measurement == "ms_since_boot":
            flightTime = data[0].value
        else:
            db.handleData(data, dbClient, flightTime)

    #handle engine controller data
    elif data[0].source == "engine":
        #update time
        if data[0].measurement == "ms_since_boot":
            engineTime = data[0].value
        else:
            db.handleData(data, dbClient, engineTime)

