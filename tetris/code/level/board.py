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

        
    def update(self, direction):
        self._clear_and_move_rows()
        if not self.game_over:
            self._check_next_figure_move()
            self.figure.move_figure(direction)

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
            
    def _is_game_over(self, position):
        for item in self.positions[0]:
            if item == 1:
                return True
        return False
        
    def _is_figure_exist_in_board(self, position):
        return position[1] < 0
    
    def _is_figure_should_stop(self, position):
        return position[1] == 18 or self.positions[position[1]+1][position[0]] == 1
    
    def _is_row_full(self, row):
        for postion in self.positions[row]:
            if postion == 0:
                return False
        return True
    
    def _remove_row(self, row):
        positions = []
        for index in range(len(self.positions[-1])):
            position = [index, row]
            self.positions[position[1]][position[0]] = 0
            positions.append(position)
        for figure in self.figures:
            figure.remove_tiles_at_postions(positions)
            
    def _move_figures(self, row):
        for figure in self.figures:
            figure.move_tiles_at_row(row)
        self.positions.pop(row)
        self.positions.insert(0, [0 ,0 ,0 ,0 ,0, 0, 0, 0, 0])
        
    def _clear_and_move_rows(self):
        for i in range(len(MAP) -1, -1, -1):
            if self._is_row_full(i):
                self._remove_row(i)
                self._move_figures(i)
            
    def fill_row(self, row):
        for index in range(len(self.positions[-1])):
            position = [index, row]
            self.positions[position[1]][position[0]] = 1
            figure = Figure(self.display_surface)
            figure.one_tile_figure(position)
            self.figures.append(figure) 