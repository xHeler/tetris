from turtle import position
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
        
        # tiles list
        self.tiles = []
        self.active_tiles = [] # actual moving figure
        
        # game over
        self.game_over = False
        
        # shape
        self.shape = Shape(SHAPES_PATH)
        
        # color
        self.color = Color()
        
    def update(self):
        if not self.game_over:
            self._check_next_tile_move()
            self._move_active_tiles()

    def draw(self):
        for tile in (self.tiles + self.active_tiles):
            tile.draw(self.display_surface)

    def add_random_figure(self):
        color = self.color.get_color()
        positions = self.shape.get_random_shape()
        for position in positions:
            self.active_tiles.append(Tile(position, color))
            
    def _add_figure_status(self):
        for tile in self.active_tiles:
            position = tile.position
            self.positions[position[1]][position[0]] = 2
            
    def _check_next_tile_move(self):
        for tile in self.active_tiles:
            position = tile.position
            if position[1] < 0:
                return
            if position[1] == 18 or self.positions[position[1]+1][position[0]] == 2:
                if self._is_game_over(position):
                    self.active_tiles = []
                    self.tiles = []
                    self.game_over = True
                    return
                self._add_figure_status()
                self.tiles += self.active_tiles
                self.active_tiles = []
                self.add_random_figure()
                return
    def _move_active_tiles(self):
        for tile in self.active_tiles:
            tile.update()
            
    def _is_game_over(self, position):
        if position[1] == 0 and self.positions[position[1]+1][position[0]] == 2:
            return True
        else:
            return False    