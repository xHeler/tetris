# -*- coding: utf-8 -*-
"""Debug module

Debug's tools whose help solve broken game aspects.

Example:
    If we need to display on screen some values:

        debug("Test", 10, 10)
"""

import pygame

pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, offset_x=10, offset_y=10):
    """Display string on the specific offset.

    Note:
        The origin coordinate (x,y) = (0,0) of the screen are at top left screen.

    Args:
        info: str, Information which will be displayed.
        offset_x: int, X coordinate offset depends origin.
        offset_y: int, Y coordinate offset depends origin.
    """
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(offset_x, offset_y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
