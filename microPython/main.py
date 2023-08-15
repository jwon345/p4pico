from machine import Pin
import time
  

led = Pin(25, Pin.OUT)
clk = Pin(1, Pin.OUT)
data = Pin(2, Pin.OUT)


Sensor = []
for Index in range(2,18):
    Sensor.append(Pin(Index,Pin.IN))



#delays to potentially allow for rising time
#in milliseconds
RiseTimers = 1
TimeOn = 5
TimeOff = 5
delay_ms = 100
delay_ms_cycle = 100

def Iterate():
    #push In 0
    time.sleep_ms(TimeOn) #ON time

    clk.high()
    time.sleep_ms(RiseTimers)
    clk.low()


    #hold the 0

    time.sleep_ms(TimeOff)

while True:
    #push FirstClock
    data.high()
    led.high()

    #rise timer for rising edge clock 
    time.sleep_ms(RiseTimers) #

    #Rising edge clock
    clk.high()

    time.sleep_ms(RiseTimers)

    clk.low()
    led.low()
    data.low()

    #printing to serial

    # print(str(gData1.value()) + str(gData2.value()) + str(gData3.value()) + str(gData4.value()))

    Svalue = 0

    ledIndex = 0
    for LED in range(0,32):
        sensA = 0
        sensB = 0
        sensC = 0
        for C in range(5,-1,-1): # sensors 0,1,2,3,4,5
            sensC <<= 1
            sensC += Sensor[C].value()
            led.toggle()
            time.sleep_ms(delay_ms)
        for B in range(11,5,-1): # sensors 6,7,8,9,10,11
            sensB <<= 1
            sensB += Sensor[B].value()
            led.toggle()
            time.sleep_ms(delay_ms)
        for A in range(15,11,-1): #sensors 12,13,14,15
            sensA <<= 1
            sensA += Sensor[A].value()
            led.toggle()
            time.sleep_ms(delay_ms)
        #iterate
        print(chr(LED + 64)+chr(sensA+64)+chr(sensB+64)+chr(sensC+64))
        time.sleep_ms(delay_ms_cycle)
        Iterate()
