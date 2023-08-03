import math

def calculatePositioning(number, Radius, screenMidX, screenMidY):
    sensorArray = []
    for n in range(0,number):
        if n==0:
            dX = math.sin((math.pi*2*number)) * Radius;
            dY = math.cos((math.pi*2*number)) * Radius;
            sensorArray.append([
                n, 
                (int)(screenMidX+dX+0.5),
                (int)(screenMidY-dY+0.5),
            ])
            continue
        dX = math.sin((math.pi*number)/n) * Radius;
        dY = math.cos((math.pi*number)/n) * Radius;
        sensorArray.append([
            n, 
            (int)(screenMidX+dX+0.5),
            (int)(screenMidY-dY+0.5),
        ])
    
    return sensorArray


print(calculatePositioning(10,10,50,50))