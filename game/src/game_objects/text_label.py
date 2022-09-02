# -*- coding: utf-8 -*-
"""Text Label

Tool to prepare and display text label on screen.
"""

import pygame

from src.utils.settings import FONT_PATH


class TextLabel:
    """Text Label Class

    Attribiutes:
        color, tuple(int, int, int), RGB color as tuple. Max value 255 (white).
        center, tuple(int, int), Coordinates of text center.
        font, Font, Pygame font object.
        surface, Surface, Element displayed on screen.
    """

    def __init__(self, text, font_size, center):
        """Constructor

        Attribiutes:
            color, tuple(int, int, int), RGB color as tuple. Max value 255 (white).
            center, tuple(int, int), Coordinates of text center.
            font, Font, Pygame font object.
            surface, Surface, Element displayed on screen.
        """
        self.color = (255, 255, 255)
        self.center = (center)

        self.font = pygame.font.Font(FONT_PATH, font_size)
        self.change_text(text)
        self.surface.get_rect().center = self.center

    def change_text(self, text):
        """Change text

        Changing displayed text message.

        Arguments:
            text: str, Message which will be displayed.
        """
        self.surface = self.font.render(text, False, self.color)

    def update(self):
        """Update

        Update element position and draw.
        """
        pygame.display.get_surface().blit(self.surface, self.center)
