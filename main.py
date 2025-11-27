import pygame
import math
from model_classes import Planet
from constants import WIDTH, HEIGHT, WHITE, YELLOW
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

    planets = [sun]

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
