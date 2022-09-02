# -*- coding: utf-8 -*-
"""Button

Interactive rectangle working like button.
"""
import pygame

from src.utils.settings import FONT_PATH


class Button:
    """Button class

    Attribiutes:
        font, Font: Pygame font class.
        input_rect: Rect, Rectangle object.
        background_color: Color, Color of button.
        text_color: Color, Text label color.
        text_surface: Surface, Object which will be displayed.
    """

    def __init__(self, text, width, height, center):
        """Constructor

        Arguments:
            text: str, Text label message.
            width: int, Width of button in pixels.
            height: int, Height of button in pixels.
            center: tuple(int, int), Center cordinate of button.

        Attribiutes:
            font, Font: Pygame font class.
            input_rect: Rect, Rectangle object.
            background_color: Color, Color of button.
            text_color: Color, Text label color.
            text_surface: Surface, Object which will be displayed.
        """
        self.font = pygame.font.Font(FONT_PATH, 22)

        # create rectangle
        self.input_rect = pygame.Rect(0, 0, width, height)
        self.input_rect.center = center

        # colors
        self.background_color = pygame.Color(48, 39, 42)
        text_color = pygame.Color('white')

        self.text_surface = self.font.render(text, True, text_color)

    def is_button_pressed(self, event):
        """Is button pressed

        Arguments:
            event: Event, Pygame event object.

        Return:
            bool, If button was pressed, return true, else return false.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.change_button_color('gray')
                return True
        return False

    def change_button_color(self, color_text='white'):
        """Change button color

        Change button background color.

        Arguments:
            color_text: str, Name of color.
        """
        self.background_color = pygame.Color(color_text)

    def update(self):
        """Update

        Update position, text and draw button.`
        """
        height = self.text_surface.get_height() / 2
        width = self.text_surface.get_width() / 2
        display_surface = pygame.display.get_surface()
        pygame.draw.rect(display_surface,
                         self.background_color, self.input_rect)
        display_surface.blit(
            self.text_surface, (self.input_rect.center[0] - width,
                                self.input_rect.center[1] - height))
