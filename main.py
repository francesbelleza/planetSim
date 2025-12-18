import pygame
import math
from model_classes import Planet
from constants import WIDTH, HEIGHT, WHITE, YELLOW, BLUE, RED, DARK_GREY
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#infinite loop that runs throughout
#the entire simulation to keep running
# ---- EVENT LOOP ----
def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.989*10e30)
    sun.sun = True

    earth = Planet(-1*Planet.AU, 0, 16, BLUE, 5.9742*10e24)

    mars = Planet(-1.524*Planet.AU, 0, 12, RED, 6.39*10e23)

    mercury = Planet(0.37*Planet.AU, 0, 8, DARK_GREY, 0.33010e24)

    venus = Planet(0.723*Planet.AU, 0, 14, WHITE, 4.8685*10e24)

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60) #60 is fps

        # this for loop is for different events happening in the sim
        # we only care about the user clicking the x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

        for planet in planets:
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()

main()
