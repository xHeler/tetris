# -*- coding: utf-8 -*-
"""Level staff

Drawing objects and updates their positions in game loop.
"""

import pygame

from src.game_world.board import Board
from src.utils.delay import Delay
from src.utils.scoreboard import Scoreboard
from src.utils.settings import HEIGHT, WIDTH, BACKGROUND_PATH, COOLDOWN
from src.entities.player import Player
from src.utils.network import Network


class Level:
    """Class configure and define game.

    Attribiutes:
        display_surface: Surface, Main screen surface where all objects will displayed.
        background_surface, Surface, Surface where background exist.
        background_rectangle, Rect, Rectangle filled of window size by loaded image.
    """

    def __init__(self):
        """ Level constructor.

        The constructor configure displaying tools and setup background.

        """
        # Creating background image
        self.background_surface = pygame.image.load(BACKGROUND_PATH).convert()
        self.background_surface = pygame.transform.scale(
            self.background_surface, (WIDTH, HEIGHT))
        self.background_rectangle = self.background_surface.get_rect(
            topleft=(0, 0))

        self.delay = Delay(COOLDOWN)

        # = create game board
        self.board = Board()

        # create player
        self.player = Player()

        self.scoreboard = Scoreboard()

        self.network = Network()

    def update(self):
        """ Updating postin and drawing objects.

        Put visual object on the main game display layer.
        """
        # draw background
        pygame.display.get_surface().blit(self.background_surface,
                                          self.background_rectangle.topleft)

        # player interaction
        self.player.update()
        self.change_speed()

        # reset game when it's over
        if self.board.is_game_over():
            self.network.send_score_to_server(self.player.score)
            self.board = Board()
            self.player = Player()

        # move figures after cooldown
        if self.delay.is_cooldown_left():
            self._check_rows()
            self.board.update(self.player)
        self.board.draw()
        self.scoreboard.draw(self.player.score)

    def change_speed(self):
        """ Change game speed:

        When player push space or key down, game speed increased.
        """
        if self.player.direction == -1:
            self.delay.set_cooldown(0)
        else:
            self.delay.set_cooldown(COOLDOWN)

    def _check_rows(self):
        """Checking any row is fill

        Board function return points given by full row and if it exists, add
            this score for player.
        """
        multiplier = self.board.get_points_for_full_row()
        if multiplier > 0:
            self.player.add_score(multiplier)
