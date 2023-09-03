
LED = 0b000011 + 64
A = 0b000011 + 64
B = 0b111111 + 64
C = 0b001110 + 64

#these don't matter for now
carriageReturn = 0x0f 
newLine = 0x0f


def microRead():
    return (chr(LED)+chr(A)+chr(B)+chr(C)+chr(carriageReturn)+chr(newLine))

microChars = microRead()

binLED = bin(ord(microChars[0]))
binA = bin(ord(microChars[1]))
binB = bin(ord(microChars[2]))
binC = bin(ord(microChars[3]))

Data = [binLED[4:10],binA[3:10]+binB[3:10]+binC[5:10]]

print(Data)

print(int(Data[0],2)) # turn the first index into an integer easy
print(Data[1])
for index, i in enumerate(Data[1]):
    if i == 0:
        
        print(str(index) + ":" + str(i))



# input()