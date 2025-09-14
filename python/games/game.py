import sys
import pygame 
import math

class main:
    

    def __init__(self):
        self.x , self.y = 640 , 360
        pygame.init()
        self.screen = pygame.display.set_mode((1280 , 720 ) )
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("jckawin")
        





    def run(self):
        i = 0
        while True:
            i += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT] :
                self.x += 20
            if key_pressed[pygame.K_LEFT]:
                self.x -=20
            if key_pressed[pygame.K_DOWN] :
                self.y += 20
            if key_pressed[pygame.K_UP]:
        
                self.y -=20

            else: 
                self.x += math.cos(i)
                self.y += math.sin(i)
            self.screen.fill("Green")
            
            self.rect = pygame.rect.Rect(self.x , self.y , 40 , 50 )
            self.rectagle = pygame.draw.rect(self.screen , "Red" , self.rect )
            pygame.display.flip()
            self.clock.tick(60)
            



player : main = main()
player.run()

