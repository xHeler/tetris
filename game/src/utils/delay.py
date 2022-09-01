# -*- coding: utf-8 -*-
""" Delay tools

Class support doing things after specific delay during the game.
"""
import pygame


class Delay:
    """Class Delay

    Attribiutes:
        last: int, Store number of ticks during the game.
        cooldown: int, Positive number define time between two actions in
            miliseconds.
    """

    def __init__(self, cooldown):
        """Constructor

        Setup last catched ticks.

        Attribiutes:
            last: int, Store number of ticks during the game.
            cooldown: int, Positive number define time between two actions in
                miliseconds.
        """
        self.last = pygame.time.get_ticks()
        self._cooldown = cooldown

    def is_cooldown_left(self):
        """Check cooldown left

        Do something when cooldown left.

        #Todo:
            * change to universal
        """
        now = pygame.time.get_ticks()
        if now - self.last >= self._cooldown:
            self.last = now
            return True
        return False

    def set_cooldown(self, cooldown):
        """Set cooldown value

        Arguments:
            cooldown: int, Time in milliseconds.
        """
        if cooldown < 0:
            return
        self._cooldown = cooldown
