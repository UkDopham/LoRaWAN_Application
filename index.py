import sys,os, time
import platform
from random import randint
import serial,serial.tools.list_ports #pip install pyserial


def find_USB_device():
    myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    print(myports)
    usb_port_list = [p[0] for p in myports]
    
    return usb_port_list

def readData(self):
        self.serial.flush() # it is buffering. required to get the data out *now*
        answer=""
        while  self.serial.inWaiting()>0: #self.serial.readable() and
            answer += "\n"+str(self.serial.readline()).replace("\\r","").replace("\\n","").replace("'","").replace("b","")
        return answer    

find_USB_device()

ser = serial.Serial(
    port='COM5',\
    baudrate=57600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

while (True):
	print(ser.readline())
