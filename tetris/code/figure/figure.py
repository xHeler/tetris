from turtle import pos
from utils.settings import SHAPES_PATH
from figure.color import Color
from figure.shape import Shape
from figure.tile import Tile


class Figure:
    def __init__(self, display_surface, visible = False):
        # display surface
        self.display_surface = display_surface
        
        # shape
        self.shape = Shape(SHAPES_PATH)
        
        # tiles
        self.tiles = []
        
        # color
        self.color = Color()
        
        # build figure
        self._build_figure()
        
        # visible
        self.visible = visible
        
    def draw(self):
        for tile in self.tiles:
            tile.draw(self.display_surface)
            
    def move_figure(self, direction, positions):
        if direction == 1 and self._is_move__left_possible(positions):
            for tile in self.tiles:
                tile.move_down_one_position()
                tile.move_left_one_position()
        elif direction == 2 and self._is_move__right_possible(positions):
            for tile in self.tiles:
                tile.move_down_one_position()
                tile.move_right_one_position()
        else:
            for tile in self.tiles:
                tile.move_down_one_position()
            
    def get_tiles_positions(self):
        list = []
        for tile in self.tiles:
            list.append(tile.position)
        return list
    
    def remove_tiles_at_postions(self, positions):
        for position in positions:
            self.remove_tile_at_position(position)
    
    def remove_tile_at_position(self, position):
        for tile in self.tiles:
            if tile.position == position:
                self.tiles.remove(tile)
                
    def move_tiles_at_row(self, row):
        for tile in self.tiles:
            if tile.position[1] <= row:
                tile.move_down_one_position()
                
    def change_visible(self, visible):
        self.visible = visible
        for tile in self.tiles:
            tile.visible = self.visible

    def _build_figure(self):
        color = self.color.get_color()
        positions = self.shape.get_random_shape()
        for position in positions:
            self.tiles.append(Tile(position, color))
            
    def _is_move__right_possible(self, positions):
        for position in self.get_tiles_positions():
            if position[0] == 8:
                return False
            if position[1] < 0:
                continue
            if positions[position[1]][position[0] + 1] == 1:
                return False
        return True

    def _is_move__left_possible(self, positions):
        for position in self.get_tiles_positions():
            if position[0] == 0:
                return False
            if position[1] < 0:
                continue
            if positions[position[1]][position[0] - 1] == 1:
                return False
        return True
    
    def one_tile_figure(self, position):
        color = self.color.get_color()
        self.tiles = []
        self.tiles.append(Tile(position, color, True))