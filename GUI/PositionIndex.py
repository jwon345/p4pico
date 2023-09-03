import math

def calculatePositioning(number, Radius, screenMidX, screenMidY, offset = 0.0):
    positionArray = []
    if offset != 0:
        for n in range(0,number):
            if n==0:
                dX = math.sin(((math.pi*2) + offset)) * Radius
                dY = math.cos(((math.pi*2) + offset)) * Radius
                positionArray.append([
                    n, 
                    (int)(screenMidX+dX+0.5), #0.5 for integer round down
                    (int)(screenMidY-dY+0.5),
                ])
                continue
            dX = math.sin(((2*math.pi) * (n/number)) + offset) * Radius
            dY = math.cos(((2*math.pi) * (n/number)) + offset) * Radius
            positionArray.append([
                n, 
                (int)(screenMidX+dX+0.5),
                (int)(screenMidY-dY+0.5),
            ])
        return positionArray 
    
    for n in range(0,number):
        if n==0:
            dX = math.sin((math.pi*2)) * Radius
            dY = math.cos((math.pi*2)) * Radius
            positionArray.append([
                n, 
                (int)(screenMidX+dX+0.5), #0.5 for integer round down
                (int)(screenMidY-dY+0.5),
            ])
            continue
        dX = math.sin((2*math.pi) * (n/number)) * Radius
        dY = math.cos((2*math.pi) * (n/number)) * Radius
        positionArray.append([
            n, 
            (int)(screenMidX+dX+0.5),
            (int)(screenMidY-dY+0.5),
        ])
    return positionArray 

LEDArrayIndex = [
    3,2,1,0,
    7,6,5,4,
    11,10,9,8,
    15,14,13,12,
    19,18,17,16,
    23,22,21,20,
    27,26,25,24,
    31,30,29,28]

# print(calculatePositioning(4,50,50,50))
# input() # stop close