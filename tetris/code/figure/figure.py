from utils.settings import SHAPES_PATH
from figure.color import Color
from figure.shape import Shape
from figure.tile import Tile


class Figure:
    def __init__(self, display_surface):
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
        
    def draw(self):
        for tile in self.tiles:
            tile.draw(self.display_surface)
            
    def move_figure(self, direction):
        if direction == 1 and self._is_move__left_possible():
            for tile in self.tiles:
                tile.move_down_one_position()
                tile.move_left_one_position()
        elif direction == 2 and self._is_move__right_possible():
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
    
    def _build_figure(self):
        color = self.color.get_color()
        positions = self.shape.get_random_shape()
        for position in positions:
            self.tiles.append(Tile(position, color))
            
    def _is_move__right_possible(self):
        for position in self.get_tiles_positions():
            if position[0] == 8:
                return False
        return True
    
    def _is_move__left_possible(self):
        for position in self.get_tiles_positions():
            if position[0] == 0:
                return False
        return True