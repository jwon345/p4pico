##This file will just be used to output the theoretical outputs  

from machine import Pin
import time
testNumber = 0
Led = Pin(25, Pin.OUT)
delay_ms = 100
while True:

    

    for I in range(1,32):
        Led.high()
        time.sleep_ms(delay_ms)

        # reading and printing all the sensor values
        print(I)
        print(0b0011111) #ideally uint 5
        print(0b000111111111111)

        Led.low()
        time.sleep_ms(delay_ms)


    print("looped")