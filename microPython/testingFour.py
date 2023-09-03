from machine import Pin
import time
  

led = Pin(25, Pin.OUT)
clk = Pin(1, Pin.OUT)
data = Pin(2, Pin.OUT)




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

    print("iterate")

    time.sleep_ms(delay_ms_cycle)
    Iterate()
