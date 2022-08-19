# -*- coding: utf-8 -*-
"""Figure

Some tiles setup in specific shape and color build figure.
"""
from src.utils.settings import SHAPES_PATH
from src.game_objects.color import Color
from src.game_objects.shape import Shape
from src.game_objects.tile import Tile


class Figure:
    """Figure class

    Movement of figure, drawing and building.

    Attribiutes:
        display_surface: Surface, Main screen surface where all objects will
                displayed.
        shape: Shape, Take randomly shape from shape list, get prepared positions.
        tiles: list, Tiles whoes build a figure.
        color, Color, Take next color depends on order.
        visible, bool, Define visibility of figure.
    """
    def __init__(self, display_surface, visible = False):
        """"Constructor

        Attribiutes:
            display_surface: Surface, Main screen surface where all objects will
                    displayed.
            shape: Shape, Take randomly shape from shape list, get prepared positions.
            tiles: list, Tiles whoes build a figure.
            color, Color, Take next color depends on order.
            visible, bool, Define visibility of figure.

        Args:
            display_surface: Surface, Inlude origin display surface.
            visible: bool, Set visibilty of figure. Default = False.
        """
        self.display_surface = display_surface
        self.shape = Shape(SHAPES_PATH)
        self.tiles = []
        self.color = Color()
        self.visible = visible

    def draw(self):
        """Drawing all tiles from list
        """
        for tile in self.tiles:
            tile.draw(self.display_surface)

    def move_figure(self, direction, positions):
        """Moving figure in direction

        If the next move is possible, move the figure in left or right and one block down.
        """
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
        """Get tiles positions

        Return:
            tiles_positions: list, List includes all tiles positions.
        """
        tiles_positions = []
        for tile in self.tiles:
            tiles_positions.append(tile.position)
        return tiles_positions

    def remove_tiles_at_postions(self, positions):
        """Remove tiles from positions
        """
        for position in positions:
            self.remove_tile_at_position(position)

    def remove_tile_at_position(self, position):
        """Remove single tile from position

        If tile exist in postion, then remove that.
        """
        for tile in self.tiles:
            if tile.position == position:
                self.tiles.remove(tile)

    def move_tiles_above_row(self, row):
        """Move tile above the row

        Move down all tiles above row index.
        """
        for tile in self.tiles:
            if tile.position[1] <= row:
                tile.move_down_one_position()

    def change_visible(self, visible):
        """Change figure visibility

        Args:
            visible, bool, State of visibility.
        """
        self.visible = visible
        for tile in self.tiles:
            tile.visible = self.visible

    def build_one_tile_figure(self, position):
        """Build one tile figure
        """
        color = self.color.get_next_color()
        self.tiles = []
        self.tiles.append(Tile(position, color, True))

    def build_figure(self):
        """Build figure with tiles
        """
        color = self.color.get_next_color()
        positions = self.shape.get_random_shape()
        for position in positions:
            self.tiles.append(Tile(position, color))

    def _is_move__right_possible(self, positions):
        """Check possibility of right move

        Args:
            positions: list, List with all positions on map.

        Return:
            bool, If move is possible, return True.
        """
        for position in self.get_tiles_positions():
            if position[0] == 8:
                return False
            if position[1] < 0:
                continue
            if positions[position[1] + 1][position[0] + 1] == 1:
                return False
        return True

    def _is_move__left_possible(self, positions):
        """Check possibility of left move

        Args:
            positions: list, List with all positions on map.

        Return:
            bool, If move is possible, return True.
        """
        for position in self.get_tiles_positions():
            if position[0] == 0:
                return False
            if position[1] < 0:
                continue
            if positions[position[1] + 1][position[0] - 1] == 1:
                return False
        return True
