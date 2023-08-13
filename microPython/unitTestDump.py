##This file will just be used to output the theoretical outputs  
import machine
from machine import Pin
import time
testNumber = 0
Led = Pin(25, Pin.OUT)
delay_ms = 1
delay_ms_cycle = 500

machine.freq(240000000) # type: ignore

while True:
    ledIndex = 0
    for LED in range(0,32):
        sensA = 0
        sensB = 0
        sensC = 0
        for C in range(0,7):
            # print(i) # LED index
            sensC <<= 1
            sensC += 1
            # print(bytes([sensA])+bytes([sensB])+bytes([sensC]))
            print(chr(LED + 64)+chr(sensA)+chr(sensB)+chr(sensC))
            Led.toggle()
            time.sleep_ms(delay_ms)
        for B in range(0,7):
            # print(i) # LED index
            sensB <<= 1
            sensB += 1
            print(chr(LED + 64)+chr(sensA)+chr(sensB)+chr(sensC))
            Led.toggle()
            time.sleep_ms(delay_ms)
        for A in range(0,7):
            # print(i) # LED index
            sensA <<= 1
            sensA += 1
            print(chr(LED + 64)+chr(sensA)+chr(sensB)+chr(sensC))
            Led.toggle()
            time.sleep_ms(delay_ms)
        #iterate
        time.sleep_ms(delay_ms_cycle)


    print("looped")
