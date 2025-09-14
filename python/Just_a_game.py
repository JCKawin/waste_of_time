import sys

import pygame
from pygame import sprite


class all(sprite):
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1200, 600))

    def runner(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            pygame.display.update()


a: all = all()
a.runner()
