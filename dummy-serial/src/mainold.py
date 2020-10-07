import serial
import serial.tools.list_ports
import sys
import time

#combines a bytestring to a single int. Little endian
def combineBytes(bytes):
    total = 0
    count = 0
    for v in bytes:
        total += v << (count * 8)
        count += 1
    return total

#tries to initialize a device
def initDevice(ser):
    ser.write(b'aaa')
    if (ser.read(3) == b'bbb'):
        print("yay")
        return 1
    print("nay")
    return 0

#tries to find and initialize the correct port
def openSerial(ser):
    ports = serial.tools.list_ports.grep("ACM")
    for v in ports:
        ser.port = v.device
        ser.open()
        print("Testing" + str(v))
        if initDevice(ser):
            print("Succesfully connected")
            return True
        ser.close()
    else:
        print("could not open serial connection")
        return False

ser = serial.Serial()
ser.baudrate = 11520
initialized = openSerial(ser)

while initialized:
    print(combineBytes(ser.read(4)))