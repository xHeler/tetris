# -*- coding: utf-8 -*-
"""Level staff

Drawing objects and updates their positions in game loop.
"""

import pygame

from settings import HEIGHT, WIDTH, BACKGROUND_PATH
from tile import Tile


class Level:
    """Class configure and define game.

    Attribiutes:
        display_surface: Surface, Main screen surface where all objects will displayed.
        background_surface, Surface, Surface where background exist.
        background_rectangle, Rect, Rectangle filled of window size by loaded image.
    """
    def __init__(self):
        """ Level constructor.

        The constructor configure displaying tools and setup background.

        """
        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprites group
        self.sprites = pygame.sprite.Group()

        # Creating background image
        self.background_surface = pygame.image.load(BACKGROUND_PATH).convert()
        self.background_surface = pygame.transform.scale(self.background_surface, (WIDTH, HEIGHT))
        self.background_rectangle = self.background_surface.get_rect(topleft=(0, 0))


        #! Create testing tile by specific color
        for row in range(19):
            for column in range(9):
                Tile(self.sprites, (column, row), 'green')

    def update(self):
        """ Updating postin and drawing objects.

        Put visual object on the main game display layer.
        """
        self.display_surface.blit(self.background_surface,
                                  self.background_rectangle.topleft)
        self.sprites.draw(self.display_surface)
        self.sprites.update()