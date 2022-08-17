# -*- coding: utf-8 -*-
""" Delay tools

Class support doing things after specific delay during the game.
"""
import pygame


class Delay:
    """Class Delay

    Attribiutes:
        cooldown: int, Positive number define time between two actions in
            miliseconds.
    """
    def __init__(self, cooldown):
        """Constructor

        Setup last catched ticks.
        """
        self.last = pygame.time.get_ticks()
        self.cooldown = cooldown

    def is_cooldown_left(self):
        """Check cooldown left

        Do something when cooldown left.

        Todo:
            * change to universal
        """
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            return True
        return False