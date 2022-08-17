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
            
    def move_figure_down(self):
        for tile in self.tiles:
            tile.update()
    
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