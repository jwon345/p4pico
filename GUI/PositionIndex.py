import math

def calculatePositioning(number, Radius, screenMidX, screenMidY):
    sensorArray = []
    for n in range(0,number):
        if n==0:
            dX = math.sin((math.pi*2)) * Radius
            dY = math.cos((math.pi*2)) * Radius
            sensorArray.append([
                n, 
                (int)(screenMidX+dX+0.5), #0.5 for integer round down
                (int)(screenMidY-dY+0.5),
            ])
            continue
        dX = math.sin((2*math.pi) * (n/number)) * Radius
        dY = math.cos((2*math.pi) * (n/number)) * Radius
        sensorArray.append([
            n, 
            (int)(screenMidX+dX+0.5),
            (int)(screenMidY-dY+0.5),
        ])
    
    return sensorArray

# testing
print(calculatePositioning(4,50,50,50))
input() # stop close