import serial 
import math
import pygame
from sys import platform
import time
from PositionIndex import calculatePositioning

###User definition
numberSensors = 16
numberLEDs = 32

SensorOffset = 1/numberLEDs * 2 * math.pi * 0.5

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
        ser = serial.Serial('/dev/ttyACM0',9600) 
    elif platform == "win32": 
        ser = serial.Serial('COM3',9600) 
    else:
        print("tf operating system?")
    connected = True
except:
    connected = False
    print("couldn't connect for some reason")

#Pygame for GUI

pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))

#Quit condition
run = True

#Graphical positions of sensors

sensors = [[400,350], [450,300], [450,200],[400,150]]
#Graphical postion of LED
led = [200,250]
#States of the LED to be varriable
sensorStates = [True,False,False,False]

LEDS = calculatePositioning(numberLEDs,radius,screenHeight/2,screenWidth/2)

Sensors = calculatePositioning(numberSensors,radius,screenHeight/2,screenWidth/2, offset=SensorOffset)

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

    pygame.draw.circle(screen, "black", led,10)

  

    pygame.draw.circle(screen, "red" if sensorStates[0] else "blue", sensors[0],10)

    pygame.draw.circle(screen, "red" if sensorStates[1] else "blue", sensors[1],10)

    pygame.draw.circle(screen, "red" if sensorStates[2] else "blue", sensors[2],10)

    pygame.draw.circle(screen, "red" if sensorStates[3] else "blue", sensors[3],10)

  

    #Reading the COM3 line. This is blocking?
    if connected:
        reading = ser.readline().decode()
        #Debug print
        print(reading)
    else:
        reading = [0,0,0,0]


    for i in range(0,4):

        if reading[i] == "1":

            # print(str(i) + " is true")

            pygame.draw.line(screen,"red",led,sensors[i], 2)

            sensorStates[i] = True

        else:

            sensorStates[i] = False

  

    pygame.display.flip()
  

pygame.quit()