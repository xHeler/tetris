# -*- coding: utf-8 -*-
"""Single tile object

Configure, display and update single tile objects and place at specific
postion on gameboard.

Example:
    Creating Tile object:

        Tile(self.sprites, (column, row), 'green)
"""
from os import walk

import pygame

from utils.settings import TILESIZE, OFFSET_WIDTH, OFFSET_HEIGHT



class Tile(pygame.sprite.Sprite):
    """ Tile class

    Attribiutes:
        image: Surface, Loaded specific color of tile.
        rect: Rect, Rectangle layer of image object, setup with specific offset
            and position.
    """
    def __init__(self, position, color, visible=False):
        """ Tile constructor

        Load all possible tiles color to dictionary, then chose specific color
            and load image. Prepare rect at specific offset and column, row.

        Args:
            groups: Group, Group of sprites where Tile will be existing.
            position: Tuple(int, int), Row and column on map where tile exist.
                Range row = [0: 18], column = [0: 8].
            color: str, Specific color of tile.
                Example:
                    color = 'green'
        """
        super().__init__()

         # Get specific image from dictionary by color
        colors = get_graphics_dictionary('../graphics/tiles')
        self.image = colors[color]
        
        self.position = position
        self.topleft = [OFFSET_WIDTH + position[0] * TILESIZE,
                        OFFSET_HEIGHT + position[1] * TILESIZE]

        # Rescale image and set position
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = self.topleft)
        
        # visible
        self.visible = visible
        
        # stop
        self.stop = False

    def update(self):
        """Move tile one level down.
        """
        self._move_down_one_position()
    
    def draw(self, display_surface):
        if self.visible:
            display_surface.blit(self.image, self.rect.topleft)
            
    def _move_down_one_position(self):
        self.position[1] += 1
        self.topleft[1] += TILESIZE        
        self.rect.topleft = self.topleft
        if self.position[1] == 0:
            self.visible = True


def get_graphics_dictionary(path):
    """ Make dictionary of objects at specific path

    At this moment all image files should be .png or .jpg.

    Example:
        get_graphics_dictionary('../graphics/tiles')

    Returns:
        Dictionary with keys and image surface as values.

    TODO:
        * possible else image extensions
    """
    surface_dictionary = {}
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_dictionary[image[:-4]] = image_surface
    return surface_dictionary
