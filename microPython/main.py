from machine import Pin
import time

  

led = Pin("LED", Pin.OUT)
clk = Pin(2, Pin.OUT)
data = Pin(3, Pin.OUT)
pin1 = Pin(1,Pin.OUT)

  

gData1 = Pin(16, Pin.IN)
gData2 = Pin(17, Pin.IN)
gData3 = Pin(18, Pin.IN)
gData4 = Pin(19, Pin.IN)

#delays to potentially allow for rising time

#in milliseconds

RiseTimers = 1
TimeOn = 10
TimeOff = 20

pin1.high()

while True:
    #push FirstClock
    data.high()
    led.high()

    time.sleep_ms(RiseTimers) #

    clk.high()

    time.sleep_ms(RiseTimers)

    clk.low()
    led.low()
    data.low()

    #printing to serial

    print(str(gData1.value()) + str(gData2.value()) + str(gData3.value()) + str(gData4.value()))

    #push In 0
    time.sleep_ms(TimeOn)
    clk.high()
    time.sleep_ms(RiseTimers)
    clk.low()
    data.low()

    #hold the 0

    time.sleep_ms(TimeOff)