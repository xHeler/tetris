from debug import debug
import pygame

class Player:
    def __init__(self):
        self.direction = 0
    
    def update(self):
        self.input()
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = 1
        elif keys[pygame.K_RIGHT]:
            self.direction = 2
        elif keys[pygame.K_SPACE] or keys[pygame.K_DOWN]:
            self.direction = -1
        else:
            self.direction = 0
            