from operator import pos
from turtle import position
from settings import MAP
import pygame

from tile import Tile


class Board:
    def __init__(self):
        # tiles position map 
        self.positions = MAP
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # tiles list
        self.tiles = []
        self.active_tiles = [] # actual moving figure
        
        # color id
        self.color_id = 0   

    def update(self):
        self._check_next_tile_move()
        self._move_active_tiles()
            

    def draw(self):
        for tile in (self.tiles + self.active_tiles):
            tile.draw(self.display_surface)

    def add_figure(self, type):
        colors = ['brown', 'gold', 'green', 'orange', 'yellow']
        color = colors[self.color_id]
        self.color_id += 1
        self.color_id = self.color_id % int(len(colors))
        if type == 'I':
            self.active_tiles.append(Tile([4, -1], color))
            self.active_tiles.append(Tile([4, -2], color))
            self.active_tiles.append(Tile([4, -3], color))
            self.active_tiles.append(Tile([4, -4], color))
        elif type == 'J':
            self.active_tiles.append(Tile([4, -1], color))
            self.active_tiles.append(Tile([5, -1], color))
            self.active_tiles.append(Tile([5, -2], color))
            self.active_tiles.append(Tile([5, -3], color))
            self.active_tiles.append(Tile([5, -4], color))
            
    def _add_figure_status(self):
        for tile in self.active_tiles:
            position = tile.position
            self.positions[position[1]][position[0]] = 2
            
    def _check_next_tile_move(self):
        for tile in self.active_tiles:
            position = tile.position
            if position[1] == 18 or self.positions[position[1]+1][position[0]] == 2:
                self._add_figure_status()
                self.tiles += self.active_tiles
                self.active_tiles = []
                self.add_figure('J')
                break
    def _move_active_tiles(self):
        for tile in self.active_tiles:
            tile.update()