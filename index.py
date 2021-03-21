import serial
from serial import Serial
import base64


def byte_xor(ba1, ba2):
    #return bytearray(a^b for a, b in zip(*map(bytearray, [ba1, ba2]))) 
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


APPKEYtmp = str.encode(input("Enter the APPKEY to login : "))
APPKEY = b'1234'

isPassCorrect = APPKEYtmp == APPKEY

if (isPassCorrect):
    print("Welcome !")
else:
    print("It's not the right APPKEY !")



if (isPassCorrect):
    port = input("Which port ?")

    ser = serial.Serial(
        port='/dev/ttyACM'+str(port),\
        baudrate=57600,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)

    print("Starting to read the USB DATA")

    #temperature = ((bytes[0] << 8) | bytes[1]) / 100;

    while (True):
        s = ser.readline()
        if s != b'' and s != b'\r\n' and s != b'\\r\\n':
            tempBytes = s.split()
            print("Data raw: " + str(tempBytes))
            tmpBytes = [int(tempBytes[0]),int(tempBytes[1])]            
            print("Data : " + str(tmpBytes))
            decrypt=byte_xor(tmpBytes, APPKEY)
            print(decrypt)
            #temperature = (  ((((int(tempBytes[0])<<8) + (int(tempBytes[1]))/65536.0)*165.0 ) - 40.0  ) )
            temperature = ((int(decrypt[0]) <<8) + int(decrypt[1]))/100
            print("Device : " + str(int(tempBytes[2])) + " " + str(temperature) + " C°")
            #print(byte_xor(s, APPKEY))
        #decrypt=byte_xor(ser.readline(), APPKEY)
        #if decrypt != b'':
        #    print(decrypt)