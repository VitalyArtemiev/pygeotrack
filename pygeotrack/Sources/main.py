import time
import serial
import pynmea2
from FO import FO
from GO import GO


LOCAL_LAT = 55.66922
LOCAL_LON = 37.48214
LOCAL_ALT = 1180.750

SERIAL_PORT = "/dev/ttyusb0"

obj = FO()
antenna = GO(LOCAL_LAT, LOCAL_LON, LOCAL_ALT)


def read(filename):
    f = open(filename)
    reader = pynmea2.NMEAStreamReader(f)

    while 1:
        for msg in reader.next():
            #obj.getParams(msg)
            antenna.calcDir(obj)
            antenna.printDir()


def read_serial(filename):
    com = None
    reader = pynmea2.NMEAStreamReader()

    while 1:

        if com is None:
          try:
            com = serial.Serial(filename, timeout=5.0)
          except serial.SerialException:
            print('could not connect to %s' % filename)
            time.sleep(5.0)
            continue

        if com.in_waiting > 0:
            data = com.readline()
            for msg in reader.next(data):
                #obj.getParams(msg)
                antenna.calcDir(obj)
                antenna.printDir()
        else:
            time.sleep(1.0)

read_serial(SERIAL_PORT)

read("testfile.txt")
