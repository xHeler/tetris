# -*- coding: utf-8 -*-
"""Main project game file

In this module we have Game class, where we initialize pygame and other classes
located in game. We also have if statement executed when invoked directly.

Example:
    We could execute this file in this case:

        # python main.py
"""

import sys
import pygame

from src.utils.settings import WIDTH, HEIGHT, FPS
from src.game_world.level import Level


class Game:
    """A Game class

    Class created one's in main file.

    Attributes:
        screen: Surface, The origin game window screen with specify width and
            height attached from settings file.
        clock: Clock, The game's Clock class whose possible manipulate time.
        level: Level, Level class that drawing and updating objects.
    """

    def __init__(self):
        """Game constructor.

        The constructor also setup game caption viewed on top bar of game
            window. And build Level class.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        """Run a game main loop.

        Run method's catching events during the game, display object and
            control speed of game by clock.
        """
        while True:
            self._catch_events()
            self.screen.fill('black')
            self.level.update()
            pygame.display.update()
            self.clock.tick(FPS)

    def _catch_events(self):
        """Catching events during the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
