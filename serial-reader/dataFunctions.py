class Data:
    def __init__(self, source, measurement, value):
        self.source = source #flight or engine
        self.measurement = measurement #name of data
        self.value = value

dataFunctions = {}

#ms since boot engine controller
def f0x10(ser):
    value = ser.readBytes(4)
    return [Data("engine", "ms_since_boot", value)]
dataFunctions[0x10] = f0x10

#μs since boot engine controller
def f0x11(ser):
    value = ser.readBytes(8)
    return [Data("engine", "us_since_boot", value)]
dataFunctions[0x11] = f0x11

#ms since boot flight controller
def f0x90(ser):
    value = ser.readBytes(4)
    return [Data("flight", "ms_since_boot", value)]
dataFunctions[0x90] = f0x90

#µs since boot flight controller
def f0x91(ser):
    value = ser.readBytes(8)
    return [Data("flight", "us_since_boot", value)]
dataFunctions[0x91] = f0x91


####################### made up functions
#altitude
def f0x00(ser):
    value = ser.readBytes(2)
    return [Data("flight", "altitude", value)]
dataFunctions[0x00] = f0x00

#acceleration
def f0x01(ser):
    value = ser.readBytes(1)
    return [Data("flight", "acceleration", value)]
dataFunctions[0x01] = f0x01

#pressure
def f0x02(ser):
    value = ser.readBytes(2)
    return [Data("flight", "pressure", value)]
dataFunctions[0x02] = f0x02

#catastrophe
def f0x03(ser):
    value = ser.readBytes(1)
    return [Data("engine", "catastrophe", value)]
dataFunctions[0x03] = f0x03

#gyroscope
def f0x04(ser):
    x = ser.readBytes(1)
    y = ser.readBytes(1)
    z = ser.readBytes(1)
    return [
        Data("flight", "gyroX", x),
        Data("flight", "gyroY", y),
        Data("flight", "gyroZ", z)
    ]
dataFunctions[0x04] = f0x04