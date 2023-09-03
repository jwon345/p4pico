import serial 
import math
import pygame
import pprint
from sys import platform
import time
from PositionIndex import calculatePositioning
from PositionIndex import LEDArrayIndex
from testData import microRead 


###User definition
numberSensors = 16
numberLEDs = 32

angleOffset = 0.2
SensorOffset = 1/numberLEDs * 2 * math.pi * angleOffset

screenWidth = 800
screenHeight = 800
radius = 300 

LEDsize = 5
LEDColor = "black"

sensorSize = 5
sensorColor = "red"

##
connected = False

ser = serial.Serial() # i guess init definition to remove the unbound issues
# establishing connection based on operating system
try:   
    if platform == "linux" or "linux2":
        ser = serial.Serial('/dev/ttyACM1',115200) 
    elif platform == "win32": 
        ser = serial.Serial('COM3',115200) 
    else:
        print("tf operating system?")
    connected = True
except:
    ser = serial.Serial('/dev/ttyACM0',115200) 
    connected = False
    print("couldn't connect for some reason")





#Pygame for GUI

pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))

#Quit condition
run = True

#Graphical positions of sensors

# sensors = [[400,350], [450,300], [450,200],[400,150]]
#Graphical postion of LED
led = [200,250]
#States of the LED to be varriable
sensorStates = [True,False,False,False]

LEDS = calculatePositioning(numberLEDs,radius,screenHeight/2,screenWidth/2)
Sensors = calculatePositioning(numberSensors,radius,screenHeight/2,screenWidth/2, offset=SensorOffset)

# pprint(LEDS)
# print
# input()
while run:
    #Exit handler
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

    screen.fill("white")

  
    for LED in LEDS:
        if LED[0] == 0:
            pygame.draw.circle(screen, "green", (LED[1],LED[2]),LEDsize)
            continue
        pygame.draw.circle(screen, LEDColor, (LED[1],LED[2]),LEDsize)
    for sensor in Sensors:
        pygame.draw.circle(screen, sensorColor, (sensor[1],sensor[2]),sensorSize)

    # pygame.draw.circle(screen, "black", led,10)
    # pygame.draw.circle(screen, "red" if sensorStates[0] else "blue", sensors[0],10)
    # pygame.draw.circle(screen, "red" if sensorStates[1] else "blue", sensors[1],10)
    # pygame.draw.circle(screen, "red" if sensorStates[2] else "blue", sensors[2],10)
    # pygame.draw.circle(screen, "red" if sensorStates[3] else "blue", sensors[3],10)


    ##Reads w/e number and corresponding Data
    microChars = ser.readline().decode()

    binLED = bin(ord(microChars[0]))
    binA = bin(ord(microChars[1]))
    binB = bin(ord(microChars[2]))
    binC = bin(ord(microChars[3]))

    Data = [binLED[4:10],binA[3:10]+binB[3:10]+binC[5:10]]

    print(Data)

    print("LED number = " + str(int(Data[0],2))) # turn the first index into an integer easy
    print(LEDS[int(Data[0],2)][1:3]) # turn the first index into an integer easy

    #i = ->  integer value represeting the status of the sensor
    for index, i in enumerate(Data[1]):
        if i == "1":
            #??? what is 1:3 --> LEDs is a tuple
            pygame.draw.line(screen,"black", LEDS[LEDArrayIndex[int(Data[0],2)]][1:3], Sensors[index][1:3])
        # else:
        #     pygame.draw.line(screen,"red", LEDS[LEDArrayIndex[int(Data[0],2)]][1:3], Sensors[index][1:3])

        print(str(index) + ":" + str(i))

    #Reading the COM3 line. This is blocking?
    # if connected:
    #     reading = ser.readline().decode()
    #     #Debug print
    #     print(reading)
    # else:
    #     reading = [0,0,0,0]


    # for i in range(0,4):

    #     if reading[i] == "1":

    #         # print(str(i) + " is true")

    #         pygame.draw.line(screen,"red",led,sensors[i], 2)

    #         sensorStates[i] = True

    #     else:

    #         sensorStates[i] = False

  

    pygame.display.flip() # update display
  

pygame.quit()