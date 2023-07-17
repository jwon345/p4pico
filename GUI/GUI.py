import serial 
import pygame
import time

#For serial reading

#for windows machine
#ser = Serial('COM3', 9600)

#Linux Machines
ser = serial.Serial('/dev/ttyACM0',9600) 

#Pygame for GUI

pygame.init()
screen = pygame.display.set_mode((500,500))

#Quit condition
run = True

#Graphical positions of sensors

sensors = [[400,350], [450,300], [450,200],[400,150]]
#Graphical postion of LED
led = [200,250]
#States of the LED to be varriable
sensorStates = [True,False,False,False]

while run:
    #Exit handler
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

  

    screen.fill("white")

  

    pygame.draw.circle(screen, "black", led,10)

  

    pygame.draw.circle(screen, "red" if sensorStates[0] else "blue", sensors[0],10)

    pygame.draw.circle(screen, "red" if sensorStates[1] else "blue", sensors[1],10)

    pygame.draw.circle(screen, "red" if sensorStates[2] else "blue", sensors[2],10)

    pygame.draw.circle(screen, "red" if sensorStates[3] else "blue", sensors[3],10)

  

    #Reading the COM3 line. This is blocking?


    reading = ser.readline().decode()

    #Debug print

    print(reading)

    for i in range(0,4):

        if reading[i] == "1":

            # print(str(i) + " is true")

            pygame.draw.line(screen,"red",led,sensors[i], 2)

            sensorStates[i] = True

        else:

            sensorStates[i] = False

  

    pygame.display.flip()
  

pygame.quit()