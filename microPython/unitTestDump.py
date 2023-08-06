##This file will just be used to output the theoretical outputs  
from machine import Pin
import time
testNumber = 0
Led = Pin(25, Pin.OUT)
while True:
    Led.high()
    time.sleep_us(10)
    testNumber += 1
    Led.low()
    print(testNumber)