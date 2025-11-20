import pygame
import math
pygame.init()

#sets up planet window
WIDTH, HEIGHT = 800,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("planetSim")

#infinite loop that runs throughout
#the entire simulation to keep running
# ---- EVENT LOOP ----
def main():
    run = True

    while run:
        # this for loop gets different events happening in the sim
        # we only care about the user clicking the x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

    pygame.quit()

main()
