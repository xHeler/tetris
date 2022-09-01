# -*- coding: utf-8 -*-
"""Player

Actor class take game inputs, and store information.
"""
import pygame


class Player:
    """Player class

    Attribiutes:
        direction: int, The direction of figure movement.
            Example:
                1 - left
                2 - right
                -1 - bottom
                0 - neutral
        score, int, Number of earned points.
    """

    def __init__(self):
        """Constructor

        Attribiutes:
            direction: int, The direction of figure movement.
                Example:
                    1 - left
                    2 - right
                    -1 - bottom
                    0 - neutral
            score, int, Number of earned points.
        """
        self.direction = 0
        self.score = 0

    def update(self):
        """Update player
        """
        self._input()

    def add_score(self, multiplier):
        """Add points to score

        Args:
            multiplier: int, Multiplier of added score.
        """
        self.score += multiplier * 100

    def _input(self):
        """Input keys

        Check actor integration with games. Then change direction.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = 1
        elif keys[pygame.K_RIGHT]:
            self.direction = 2
        elif keys[pygame.K_SPACE] or keys[pygame.K_DOWN]:
            self.direction = -1
