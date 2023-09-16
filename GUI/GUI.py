import serial 
import math
import pygame
import pprint
from sys import platform
import time
import shapely
from shapely.geometry import mapping
from PositionIndex import calculatePositioning
from PositionIndex import LEDArrayIndex
from testData import microRead 

pp = pprint.PrettyPrinter(2)

###User definition
numberSensors = 16
numberLEDs = 32

angleOffset = -0.2
SensorOffset = 1/numberLEDs * 2 * math.pi * angleOffset

screenWidth = 1600
screenHeight = 800
radius = 300 

LEDsize = 5
LEDColor = "black"

sensorSize = 5
sensorColor = "red"

silhouetteArrayBuffer = []
for i in range(0,32,1):
    silhouetteArrayBuffer.append([(123,123),(123,123)])

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

LEDS = calculatePositioning(numberLEDs,radius,screenHeight/2,screenWidth/4)
SensorsReversed = calculatePositioning(numberSensors,radius,screenHeight/2,screenWidth/4, offset=SensorOffset)
Sensors = SensorsReversed[::-1]

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

    ##Reads w/e number and corresponding Data
    microChars = ser.readline().decode()

    binLED = bin(ord(microChars[0]))
    binA = bin(ord(microChars[1]))
    binB = bin(ord(microChars[2]))
    binC = bin(ord(microChars[3]))

    # print(binA)
    # print(binB)
    # print(binC)

    Data = [binLED[4:10],binA[5:10]+binB[3:10]+binC[3:10]]
    #Data in the form data[0] = Lednumber, data[1]= 16 binary digits representing sensor readvalues 

    # print(Data)

    # print("LED number = " + str(int(Data[0],2))) # turn the first index into an integer easy
    # print(LEDS[int(Data[0],2)][1:3]) # turn the first index into an integer easy

    #i = ->  integer value represeting the status of the sensor

    PolygonVerticies = []
    #PolygonVerticies.append(LEDS[LEDArrayIndex[int(Data[0],2)]][1:3])
    PolygonVerticies.append([LEDS[LEDArrayIndex[int(Data[0],2)]][1] + 800,LEDS[LEDArrayIndex[int(Data[0],2)]][2]])

    LedPos = int((int(Data[0],2))/2)

    ReArrangedData = Data[1][LedPos:16] + Data[1][0:LedPos]

    #i == 0 represnts Sensor blocked
    for index, i in enumerate(ReArrangedData):
        if Data[1][index - 1] == "0":
            #PolygonVerticies.append(Sensors[index][1:3])
            PolygonVerticies.append([Sensors[index][1] + 800,Sensors[index][2]])
            continue

        if i == "1":
            #PolygonVerticies.append(LEDS[LEDArrayIndex[int(Data[0],2)]][1:3])
            PolygonVerticies.append([LEDS[LEDArrayIndex[int(Data[0],2)]][1] + 800,LEDS[LEDArrayIndex[int(Data[0],2)]][2]])
            #??? what is 1:3 --> LEDs is a tuple --> [0] = number, [1]=xpos [2]=ypos
            pygame.draw.circle(screen,"green",Sensors[index][1:3], 10,51)
            pygame.draw.line(screen,"black", LEDS[LEDArrayIndex[int(Data[0],2)]][1:3], Sensors[index][1:3])
        else:
            #PolygonVerticies.append(Sensors[index][1:3])
            PolygonVerticies.append([Sensors[index][1] + 800,Sensors[index][2]])
        #     pygame.draw.line(screen,"red", LEDS[LEDArrayIndex[int(Data[0],2)]][1:3], Sensors[index][1:3])
        print(str(index) + ":" + str(i))

    #Half the iterations based on the sensor position and add 




    #PolygonVerticies.append(Sensors[0][1:3])
    # PolygonVerticies.append([Sensors[0][1] + 800,Sensors[0][2]])
    #PolygonVerticies.append(LEDS[LEDArrayIndex[int(Data[0],2)]][1:3])
    PolygonVerticies.append([LEDS[LEDArrayIndex[int(Data[0],2)]][1] + 800,LEDS[LEDArrayIndex[int(Data[0],2)]][2]])

    # pp.pprint(PolygonVerticies)

    silhouetteArrayBuffer[int(Data[0],2)] = (PolygonVerticies)
    # pp.pprint(silhouetteArrayBuffer)


        # intersectingPolygon = (shapely.intersection(a,b,1))
    try:
        pygame.draw.polygon(screen,"green", silhouetteArrayBuffer[1])
        pygame.draw.polygon(screen,"black", silhouetteArrayBuffer[16])
    except:
        pass


    try:
        a = shapely.Polygon(silhouetteArrayBuffer[4])
        b = shapely.Polygon(silhouetteArrayBuffer[16])
        intersectingPolygon = (shapely.intersection(a,b,1.0))

        pp.pprint(a)
        pp.pprint(b)
        print('intersection')
        pp.pprint(intersectingPolygon)

        print('intersection2')

        finalCrossSection = []
        preCrossSection = (mapping(intersectingPolygon)["coordinates"])

        pp.pprint(preCrossSection)

        for i in range(0,len(preCrossSection[0])):
            finalCrossSection.append(preCrossSection[0][i])
            
        pygame.draw.polygon(screen,"green", finalCrossSection)
    except:
        print("null")


    pygame.display.flip() # update display
  

pygame.quit()