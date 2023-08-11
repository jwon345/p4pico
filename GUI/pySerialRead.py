import serial
import time
from sys import platform

ser = serial.Serial()
## Esp32?
# ser = serial.Serial('/dev/ttyUSB0',115200) 

## Con for specific OS
try:   
    if platform == "linux" or "linux2":
        # ser = serial.Serial('/dev/ttyUSB0',115200) 
        # ser = serial.Serial('/dev/ttyUSB1',115200) 
        ser = serial.Serial('/dev/ttyACM1',115200) 
        print("connected")
        
    elif platform == "win32": 
        ser = serial.Serial('COM3',9600) 
    else:
        print("tf operating system?")
    connected = True
except:
    connected = False
    print("couldn't connect for some reason")

time.sleep(1)

while True:
    try:
        print(ser.readline())
        # print(ser.readline().decode())
    except:
        try:
            time.sleep(1)
            print("dead")
            ser = serial.Serial('/dev/ttyACM0', 115200) 
            print("connected")
        except:
            pass