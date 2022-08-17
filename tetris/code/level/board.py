from figure.figure import Figure
from figure.color import Color
from utils.settings import MAP, SHAPES_PATH
import pygame
from copy import deepcopy

from figure.tile import Tile
from figure.shape import Shape



class Board:
    def __init__(self):
        # tiles position map 
        self.positions = deepcopy(MAP)
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # figures
        self.figure = Figure(self.display_surface)
        self.figures = []
        
        # game over
        self.game_over = False
        
        # shape
        self.shape = Shape(SHAPES_PATH)

        
    def update(self):
        if not self.game_over:
            self._check_next_figure_move()
            self._move_figure()

    def draw(self):
        for figure in self.figures + [self.figure]:
            figure.draw()
            
    def _add_figure_status(self):
        figure_positions = self.figure.get_tiles_positions()
        for position in figure_positions:
            self.positions[position[1]][position[0]] = 1
            
    def _check_next_figure_move(self):
        figure_positions = self.figure.get_tiles_positions()
        
        for position in figure_positions:
            if self._is_figure_exist_in_board(position):
                return
            if self._is_figure_should_stop(position):
                if self._is_game_over(position):
                    self.game_over = True
                    self.figures = []
                    return
                self._add_figure_status()
                self.figures.append(self.figure)
                self.figure = Figure(self.display_surface)
                return
            
    def _move_figure(self):
        self.figure.move_figure_down()
            
    def _is_game_over(self, position):
        for item in self.positions[0]:
            if item == 1:
                return True
        return False
        
    def _is_figure_exist_in_board(self, position):
        return position[1] < 0
    
    def _is_figure_should_stop(self, position):
        return position[1] == 18 or self.positions[position[1]+1][position[0]] == 1