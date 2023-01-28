import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()

DISPLAY = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Car Racing Game')

font = pygame.font.SysFont("Times New Roman",25)
bigFont = pygame.font.SysFont("Times New Roman" , 40)

LosingText = bigFont.render("GAME OVER",False, "black")

# colors
BLACK = (0, 0, 0)


class Road:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.road = pygame.transform.scale(pygame.image.load("road.png"),
                                           [400, 400])


class Obs:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.obs = pygame.transform.scale(pygame.image.load("obs1.png"),
                                          [50, 50])


class Car:

    def __init__(self, x, y):
        self.car = pygame.transform.scale(pygame.image.load("car.jpg"),
                                          [50, 100])
        self.x = x
        self.y = y
        self.condition = True

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


class OppositeCar(Car):

    def __init__(self, x, y):
        self.car = pygame.transform.scale(pygame.image.load("oppositeCar.png"),
                                          [50, 100])
        self.x = x
        self.y = y

    def move(self):
        self.y += 3


car1 = Car(100, 100)
car2 = OppositeCar(300, 0)

obs1 = Obs(random.randint(1, 350), -150)
obs2 = Obs(random.randint(1, 350), -50)
obs3 = Obs(random.randint(1, 350), -300)

road1 = Road(0, 0)
road2 = Road(0, 100)
road3 = Road(0, 200)
road4 = Road(0, 300)
road5 = Road(0, 400)
road6 = Road(0, 500)

roads = [road1, road2, road3, road4, road5, road6]
obss = [obs1, obs2, obs3]

clock = pygame.time.Clock()

# functions

def gameOver():
    car1.condition = False
    DISPLAY.fill("white")
    DISPLAY.blit(LosingText,(10,10))


def collision():
    car_top_left = car1.x
    car_top_right = car1.x + 50

    for obs in obss:

        obs_top_left = obs.x
        obs_top_right = obs.x + 50

        if car1.y >= obs.y and car1.y <= obs.y + 50:

            if car_top_left >= obs_top_left and car_top_left <= obs_top_right:
                gameOver()

            if car_top_right <= obs_top_right and car_top_right >= obs_top_left:
                gameOver()


def displayRoads():
    for road in roads:
        DISPLAY.blit(road.road, (0, road.y))

    for obs in obss:
        DISPLAY.blit(obs.obs, (obs.x, obs.y))


def displayCars():
    car1.display()
    car2.display()
    car2.move()


def shiftRoad():
    for obs in obss:
        obs.y += 1
        if obs.y > 400:
            obs.x = random.randint(1, 350)
            obs.y = -50
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
                if car1.x > 0:
                    car1.move_left()

            if event.key == pygame.K_d:
                if car1.x < DISPLAY.get_width() - car1.car.get_width():
                    car1.move_right()

            if event.key == pygame.K_w:
                if car1.y > 0:
                    car1.move_up()

            if event.key == pygame.K_s:
                if car1.y < DISPLAY.get_height() - car1.car.get_height():
                    car1.move_down()


while True:
    clock.tick(60)
    DISPLAY.fill(BLACK)
    collision()
    displayRoads()
    displayCars()
    handleMovement()
    shiftRoad()
    if car1.condition == False:
        gameOver()
    pygame.display.update()
