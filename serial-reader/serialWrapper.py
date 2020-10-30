import serial
import serial.tools.list_ports
import sys
from datetime import datetime
import os

class SerialWrapper:
    def __init__(self):
        self.ser = serial.Serial()

        #get file name
        now = datetime.now()
        time = now.strftime("%Y-%m-%d-%H:%M:%S")
        fileName = "tel-" + time

        #create file and directory
        try:
            dirName = "telemetry_data/" 
            os.mkdir(dirName)
        except:
            pass
        try:
            self.backup = open(dirName + fileName, "w")
        except:
            print("could not create the file: " + time)
            sys.exit()

    #read x bytes as an interger, little endian
    def readBytes(self, amount):
        bytes = self.ser.read(amount)
        self.backup.write(str(bytes));
        total = 0
        count = 0
        for v in bytes:
            total += v << (count * 8)
            count += 1
        return total

    #tries to initialize a device
    def initDevice(self, ser):
        self.ser.write(b'aaa')
        if (ser.read(3) == b'bbb'):
            print("yay")
            return 1
        print("nay")
        return 0

    #tries to find and initialize the correct port
    def openSerial(self, baud):
        ser = self.ser
        ser.baudrate = baud
        ports = self.getSafeDevices()
        for v in ports:
            ser.port = v.device
            ser.open()
            print("Testing" + str(v))
            if self.initDevice(ser):
                print("Succesfully connected")
                return 0
            ser.close()
        else:
            return 1

    #finds devices that are safe to communicate with
    def getSafeDevices(self):
        safeStrings = [
            "usb",
            "arduino",
            "ch340"
        ]
        safe_devices = []

        devices = serial.tools.list_ports.comports()

        for d in devices:
            flag = False
            for substring in safeStrings:
                if substring in d.description.lower():
                    flag = True
            if flag:
                safe_devices.append(d)

        return safe_devices