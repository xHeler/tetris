from tkinter.messagebox import NO
from turtle import position
from figure.figure import Figure
from figure.color import Color
from utils.settings import MAP, SHAPES_PATH
import pygame

from figure.tile import Tile
from figure.shape import Shape



class Board:
    def __init__(self):
        # tiles position map 
        self.positions = MAP
        
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
            self._check_next_tile_move()
            self._move_figure()

    def draw(self):
        for figure in self.figures + [self.figure]:
            figure.draw()
            
    def _add_figure_status(self):
        figure_positions = self.figure.get_tiles_positions()
        for position in figure_positions:
            self.positions[position[1]][position[0]] = 1
            
    def _check_next_tile_move(self):
        figure_positions = self.figure.get_tiles_positions()
        
        for position in figure_positions:
            if position[1] < 0:
                return
            if position[1] == 18 or self.positions[position[1]+1][position[0]] == 1:
                if self._is_game_over(position):
                    self.active_tiles = []
                    self.tiles = []
                    self.game_over = True
                    return
                self._add_figure_status()
                self.figures.append(self.figure)
                self.figure = Figure(self.display_surface)
                return
            
    def _move_figure(self):
        self.figure.move_figure_down()
            
    def _is_game_over(self, position):
        if position[1] == 0 and self.positions[position[1]+1][position[0]] == 2:
            return True
        else:
            return False    