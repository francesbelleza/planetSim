import math
import pygame

#sets up planet window
WIDTH, HEIGHT = 800,800 # in pixels
pygame.display.set_caption("planetSim")

WHITE = (255, 255, 255) #RGB value
YELLOW = (255, 255, 0)

# austronomical units, distance of earth to sun
AU = 149.6e6 * 1000
G = 6.67428e-11  # gravitational constant
SCALE = 250 / AU  # 1 AU = 100 px
TIMESTEP = 3600 * 24  # secs*hours = 1 day