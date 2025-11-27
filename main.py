import pygame
import math
from model_classes import Planet
pygame.init()

#sets up planet window
WIDTH, HEIGHT = 800,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("planetSim")

WHITE = (255, 255, 255)



#infinite loop that runs throughout
#the entire simulation to keep running
# ---- EVENT LOOP ----
def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60) #60 is fps
        #pygame.display.update()

        # this for loop is for different events happening in the sim
        # we only care about the user clicking the x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

    pygame.quit()

main()
