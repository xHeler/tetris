from cmath import inf
import pygame
import os


class Scoreboard:
    def __init__(self):
        # display surface
        self.display_surface = pygame.display.get_surface()
        path = '../graphics/telelower.ttf'
        self.font = pygame.font.Font(path, 16)
        
    def draw(self, info):
        text_surface = self.font.render(str(info), False, (255, 255, 255))
        self.display_surface.blit(text_surface, (295, 62))