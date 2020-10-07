import serial
import serial.tools.list_ports

#tries to initialize a device
def initDevice(ser):
    ser.write(b'aaa')
    if (ser.read(3) == b'bbb'):
        print("yay")
        return 1
    print("nay")
    return 0

#tries to find and initialize the correct port
def openSerial(baud):
    ser = serial.Serial()
    ser.baudrate = baud
    ports = getSafeDevices()
    for v in ports:
        ser.port = v.device
        ser.open()
        print("Testing" + str(v))
        if initDevice(ser):
            print("Succesfully connected")
            return ser
        ser.close()
    else:
        return False

#finds devices that are safe to communicate with
def getSafeDevices():
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