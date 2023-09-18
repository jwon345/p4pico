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
        print("try open Linsx")
        ser = serial.Serial('COM4',115200) 
        #ser = serial.Serial('/dev/ttyACM1',115200) 
    elif platform == "win32": 
        print("try open com4")
        ser = serial.Serial('COM4',115200) 
    else:
        print("tf operating system?")
    connected = True
except:
    ser = serial.Serial('/dev/ttyACM0',115200) 
    connected = False
    print("couldn't connect for some reason")


def draw_polygon_alpha(surface, color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)



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
# -> in a tuple [index, (x,y)]

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

    ##Reads w/e number and corresponding Data ==> each read ==> led Iteration. Per LED iteration = 16 sensor readings
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

    holderList = []
    for i in range(0,16,1):
        holderList.append(i)

    #holder list representing index

    PolygonVerticies = []
    #PolygonVerticies.append(LEDS[LEDArrayIndex[int(Data[0],2)]][1:3])
    #PolygonVerticies.append([LEDS[LEDArrayIndex[int(Data[0],2)]][1] + 800,LEDS[LEDArrayIndex[int(Data[0],2)]][2]]) # push First LED index 

    #Split the LED pos to get relative number position of the sensors
    LedPos = int((int(Data[0],2))/2)+1


    sensorsRelativeToLED = Data[1][LedPos:16] + Data[1][0:LedPos]
    newIndex = holderList[LedPos:16]+holderList[0:LedPos]

    print(sensorsRelativeToLED)

    #i == 0 represnts Sensor blocked
    #index and I needs to be reordered in teh 
    #for index, i in enumerate(Data[1]):
    for i in range(0,16,1): # per sensor reading through
        #Check -> outter are switched therefore make the 
        try:
            if sensorsRelativeToLED[i - 1] == "0":
                #PolygonVerticies.append(Sensors[index][1:3])
                PolygonVerticies.append([Sensors[newIndex[i]][1] + 800,Sensors[newIndex[i]][2]])
                continue
            if sensorsRelativeToLED[i + 1] == "0":
                #PolygonVerticies.append(Sensors[index][1:3])
                PolygonVerticies.append([Sensors[newIndex[i]][1] + 800,Sensors[newIndex[i]][2]])
                continue
            #If Left side make full tbd
        except:
            pass
        if sensorsRelativeToLED[i] == "1":
            #PolygonVerticies.append(LEDS[LEDArrayIndex[int(Data[0],2)]][1:3])
            PolygonVerticies.append([LEDS[LEDArrayIndex[int(Data[0],2)]][1] + 800,LEDS[LEDArrayIndex[int(Data[0],2)]][2]])
            #??? what is 1:3 --> LEDs is a tuple --> [0] = number, [1]=xpos [2]=ypos
            pygame.draw.circle(screen,"green",Sensors[newIndex[i]][1:3], 10,51)
            pygame.draw.line(screen,"black", LEDS[LEDArrayIndex[int(Data[0],2)]][1:3], Sensors[newIndex[i]][1:3])
        else:
            #PolygonVerticies.append(Sensors[index][1:3])
            PolygonVerticies.append([Sensors[newIndex[i]][1] + 800,Sensors[newIndex[i]][2]])
        #     pygame.draw.line(screen,"red", LEDS[LEDArrayIndex[int(Data[0],2)]][1:3], Sensors[index][1:3])
        print(str(i) + ":" + str(i))

    #Half the iterations based on the sensor position and add 






    #PolygonVerticies.append(Sensors[0][1:3])
    # PolygonVerticies.append([Sensors[0][1] + 800,Sensors[0][2]])
    #PolygonVerticies.append(LEDS[LEDArrayIndex[int(Data[0],2)]][1:3])
    #PolygonVerticies.append([LEDS[LEDArrayIndex[int(Data[0],2)]][1] + 800,LEDS[LEDArrayIndex[int(Data[0],2)]][2]])

    # pp.pprint(PolygonVerticies)

    # This one might need to un comment later if 
    # silhouetteArrayBuffer[int(Data[0],2)] = (PolygonVerticies)


    #left side polygon draw
    leftSidePolygon = []
    for verticies in PolygonVerticies:
        leftSidePolygon.append((verticies[0]-800, verticies[1]))



    #Only append when there is a silhouette generated -> all points not equal  --> kinda works
    inequalityFlag = False
    for verticies in PolygonVerticies:
        if verticies == PolygonVerticies[0]:
            continue
        else:
            inequalityFlag = True

    #make some polygon point sanitising method

    for i in range(1,len(PolygonVerticies)-2,1):
        try:
            if PolygonVerticies[i] != PolygonVerticies[i+1]:
                if PolygonVerticies[i-1] == PolygonVerticies[i+1]:
                    PolygonVerticies.pop(i)
                    print("Removed Isolated Point")
        except:
            print(":)")
            

    if inequalityFlag:
        print("Inequality ")
        silhouetteArrayBuffer.append(PolygonVerticies)        

    #rolling buffer of silhouettes  FILO
    if len(silhouetteArrayBuffer) > 32:
        silhouetteArrayBuffer.pop(0)
    # pp.pprint(silhouetteArrayBuffer)

        # intersectingPolygon = (shapely.intersection(a,b,1))
    try:
        for s in silhouetteArrayBuffer:
            draw_polygon_alpha(screen,(255,0,0,5), s)
        # pygame.draw.polygon(screen,"green", silhouetteArrayBuffer[1])
        # pygame.draw.polygon(screen,"black", silhouetteArrayBuffer[16])
    except:
        pass

    # THe issue here is the Polygons are not shaped not like a cone. 
    try:
        intersectingPolygon = shapely.Polygon(silhouetteArrayBuffer[0])
        for ii in range(0,16,1):
            a = shapely.Polygon(silhouetteArrayBuffer[ii])
            intersectingPolygon = (shapely.intersection(intersectingPolygon,a,1.0))

        # pp.pprint(a)
        # pp.pprint(b)
        # print('intersection')
        # pp.pprint(intersectingPolygon)

        print('intersection2')

        finalCrossSection = []
        preCrossSection = (mapping(intersectingPolygon)["coordinates"])

        pp.pprint(preCrossSection)

        for i in range(0,len(preCrossSection[0])):
            finalCrossSection.append(preCrossSection[0][i])

        pygame.draw.polygon(screen,"green", leftSidePolygon)

        #pygame.draw.polygon(screen,"green", finalCrossSection)
    except:
        print("null")


    pygame.display.flip() # update display
  

pygame.quit()
