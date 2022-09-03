# -*- coding: utf-8 -*-
"""Input field

Interactive filed, when active catch pressed keys.
"""
import pygame

from src.utils.settings import WIDTH


class Input:
    """Input class

    Attribiutes:
        font, Font, Pygame font object.
        password_field: password_field, When true, replace letter to stars.
        user_text: str, Text wrote by actor.
        active: bool, True if button was pressed.
        color: color, Input color.
        input_rect: Rect, Object which will be displayed.
    """

    def __init__(self, coordinates, password_field=False, border=6):
        """Constructor

        Attribiutes:
            font, Font, Pygame font object.
            password_field: password_field, When true, replace letter to stars.
            user_text: str, Text wrote by actor.
            active: bool, True if button was pressed.
            color: color, Input color.
            input_rect: Rect, Object which will be displayed.
        """
        self.font = pygame.font.Font(None, 19)
        self.password_field = password_field
        self.user_text = ''
        self.active = False
        self.color = pygame.Color(48, 39, 42)

        # create rectangle
        self.input_rect = pygame.Rect(
            coordinates[0], coordinates[1], coordinates[0] * 2.7, 26)
        self.input_rect.center = (WIDTH/2, coordinates[1])
        self.border_rect = pygame.Rect(
            coordinates[0] - border/2, coordinates[1] - border/2,
            coordinates[0] * 2.7 + border, 24 + border
        )

        self.border_rect.center = (WIDTH/2, coordinates[1] - border/2 + 3)

    def catch_events(self, event):
        """Catch events

        Check when input was pressed, and catch pressed keys.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif len(self.user_text) < 30:
                self.user_text += event.unicode

    def update(self):
        """Update

        Change positions, colors, text write and draw objects.
        """
        display_surface = pygame.display.get_surface()
        if self.password_field:
            text_length = len(self.user_text)
            text_surface = self.font.render(
                '*' * text_length, True, (255, 255, 255))
        else:
            text_surface = self.font.render(
                self.user_text, True, (255, 255, 255))
        if self.active:
            color = pygame.Color('black')
            pygame.draw.rect(display_surface,
                             color, self.border_rect)
        pygame.draw.rect(display_surface, self.color, self.input_rect)

        display_surface.blit(
            text_surface, (self.input_rect.x + 2, self.input_rect.y + 6))
