# -*- coding: utf-8 -*-
"""Main project game file

In this module we have Game class, where we initialize pygame and other classes
located in game. We also have if statement executed when invoked directly.

Example:
    We could execute this file in this case:

        # python main.py

Todo:
    * Refactor run method, it should be shortened.

"""

import sys
import pygame

from settings import WIDTH, HEIGHT, FPS


class Game:
    """A Game class

    Class created one's in main file.

    Attributes:
        screen: Surface, The origin game window screen with specify width and
            height attached from settings file.
        clock: Clock, The game's Clock class whose possible manipulate time.
    """
    def __init__(self):
        """Game constructor.

        The constructor also setup game caption viewed on top bar of game
            window.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()

    def run(self):
        """Run a game main loop.

        Run method's catching events during the game, display object and
            control speed of game by clock.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
