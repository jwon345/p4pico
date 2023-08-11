from machine import Pin
import time
  

led = Pin("LED", Pin.OUT)
clk = Pin(1, Pin.OUT)
data = Pin(2, Pin.OUT)


Sensor = []

for Index in range(2,17):
    Sensor.append(Pin(Index,Pin.IN))



#delays to potentially allow for rising time
#in milliseconds
RiseTimers = 1
TimeOn = 10
TimeOff = 20

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

    for i in range(1,32):
        print(i) # LED index
        for S in range(len(Sensor), 0): 
            Svalue += Sensor[S].Value() #adds if it's on
            Svalue <<= 1 #Shifts left
        print(Svalue)
        Iterate()
