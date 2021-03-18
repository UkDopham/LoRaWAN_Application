import serial,serial.tools.list_ports #pip install pyserial
import base64


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

APPKEY = b'thisismyappkey'


ser = serial.Serial(
    port='COM1',\
    baudrate=57600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0)

while (True):
    decrypt=byte_xor(ser.readline(), APPKEY)
    if decrypt != b'':
        print(decrypt)


