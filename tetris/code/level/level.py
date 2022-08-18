# -*- coding: utf-8 -*-
"""Level staff

Drawing objects and updates their positions in game loop.
"""

import pygame

from utils.settings import HEIGHT, WIDTH, BACKGROUND_PATH, COOLDOWN
from level.board import Board
from utils.delay import Delay
from characters.player import Player


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
        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Creating background image
        self.background_surface = pygame.image.load(BACKGROUND_PATH).convert()
        self.background_surface = pygame.transform.scale(self.background_surface, (WIDTH, HEIGHT))
        self.background_rectangle = self.background_surface.get_rect(topleft=(0, 0))

        self.delay = Delay(COOLDOWN)

        #= create game board
        self.board = Board()
        
        # create player
        self.player = Player()

    def update(self):
        """ Updating postin and drawing objects.

        Put visual object on the main game display layer.
        """
        self.display_surface.blit(self.background_surface,
                                  self.background_rectangle.topleft)
        
        # player moves
        self.player.update()
        self.change_speed()
        if self.board.game_over:
            print("Game Over. Score: ", self.player.score)
            self.board = Board()
            self.player = Player()
            
        if self.delay.is_cooldown_left():
            multiplier = self.board.clear_and_move_rows()
            if multiplier > 0:
                self.player.add_score(multiplier)
                print("Score: ", self.player.score)
            self.board.update(self.player)
        self.board.draw()

    def change_speed(self):
        if self.player.direction == -1:
            self.delay.cooldown = 0
        else:
            self.delay.cooldown = COOLDOWN