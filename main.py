import pygame, sys
from pygame.locals import QUIT

pygame.init()

DISPLAY = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Car Racing Game')

# colors
BLACK = (0, 0, 0)

class Road():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.road = pygame.transform.scale(pygame.image.load("road.png"),[400,400])


class Car():
    def __init__(self, x, y):
        self.car = pygame.transform.scale(pygame.image.load("car.jpg"), [50,100])
        self.x = x
        self.y = y

    def move_left(self):
        self.x -= 10    

    def move_right(self):
        self.x += 10

    def move_up(self):
        self.y -= 10        
      
    def move_down(self):
        self.y += 10

    def display(self):
        DISPLAY.blit(self.car, [self.x, self.y])
        

car1 = Car(100,100)

road1 = Road(0,0)
road2 = Road(0,100)
road3 = Road(0,200)
road4 = Road(0,300)
road5 = Road(0,400)
road6 = Road(0,500)

roads = [road1,road2,road3,road4,road5,road6]

clock = pygame.time.Clock()

# functions

def displayRoads():
    DISPLAY.blit(road1.road, (0,road1.y))
    DISPLAY.blit(road2.road, (0,road2.y))
    DISPLAY.blit(road3.road, (0,road3.y))
    DISPLAY.blit(road4.road, (0,road4.y))
    DISPLAY.blit(road5.road, (0,road5.y))
    DISPLAY.blit(road6.road, (0,road6.y))

def displayCars():
    car1.display()

def shiftRoad():
    for road in roads:
        road.y += 1 
        if road.y > 400:
            road.y = -road.road.get_height()

def handleMovement():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if car1.x > 0 : 
                    car1.move_left()
                
            if event.key == pygame.K_d:
                if car1.x < DISPLAY.get_width() - car1.car.get_width() :
                    car1.move_right()
                
            if event.key == pygame.K_w:
                if car1.y > 0 :
                    car1.move_up()
                    
            if event.key == pygame.K_s:
                if car1.y < DISPLAY.get_height() - car1.car.get_height():
                    car1.move_down()
    
while True:
    clock.tick(60)
    DISPLAY.fill(BLACK)
    displayRoads()
    displayCars()
    handleMovement()
    shiftRoad()
    pygame.display.update()