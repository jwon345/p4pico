import pygame
import shapely
from shapely.geometry import mapping

pygame.init()
screen = pygame.display.set_mode((800,800))

running = True
a= shapely.Polygon([(500,1),(100,100),(100,200),(200,200),(200,100),(500,1,)])
b= shapely.Polygon([(1,1),(20,100),(11,20),(200,200),(200,100),(1,1,)])

# print(shapely.intersection(a,b,1.0))
x = (shapely.intersection(a,b,1.0))
print(x)
print(mapping(x)["coordinates"])

array = []

y = (mapping(x)["coordinates"])
for i in range(0,len(y[0])):
    array.append(y[0][i])
print(array)

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.polygon(screen,"black",[(500,1),(100,100),(100,200),(200,200),(200,100),(500,1,)])
    pygame.draw.polygon(screen,"green",[(1,1),(20,100),(11,20),(200,200),(200,100),(1,1,)])
    pygame.draw.polygon(screen,"purple",array)

    pygame.display.flip()

pygame.quit()