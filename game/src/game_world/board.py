# -*- coding: utf-8 -*-
"""Game board class

This class add figures, check collisions and store positions.
"""
from copy import deepcopy

import pygame

from src.utils.settings import MAP
from src.game_objects.figure import Figure


class Board:
    """Board class

    Class store tiles positions, checks game ending, moves figures. Clear and move
        tiles after checking row is full.

    Attribiutes:
        display_surface: Surface, Main screen surface where all objects will
            displayed.
        tiles_position: list, Map coded where 0 mean empty space,
            and 1 means filled by tile.
        figure, Figure, Live moving figure, controlled by player.
        figures, list, List of stable figures.

    #TODO
     * change figure into tiles list
    """
    def __init__(self):
        """Constructor

        Get origin display surface, setup default map.

        Attribiutes:
            display_surface: Surface, Main screen surface where all objects will
                displayed.
            tiles_position: list, Map coded where 0 mean empty space,
                and 1 means filled by tile.
            figure, Figure, Live moving figure, controlled by player.
            figures, list, List of stable figures.
        """
        self.display_surface = pygame.display.get_surface()
        self.tiles_positions = deepcopy(MAP)
        self.figure = Figure(self.display_surface)
        self.figure.build_figure()
        self.figures = []

    def update(self, player):
        """ Updating board aspects

        Check and clear full rows. Move figure down and player chosen
            direction. Reset player direction to default.

        Args:
            player, Player, Class needed to get movement direction.
        """
        self._check_next_figure_move()
        self.figure.move_figure(player.direction, self.tiles_positions)
        player.direction = 0

    def draw(self):
        """Drawing all tiles

        Drawing static figures and live figure.
        """
        for figure in self.figures + [self.figure]:
            figure.draw()

    def get_points_for_full_row(self):
        """Getting points for full rows

        Check if any row is full, then remove this row, moves static figures
            down and increment points value.
        """
        points = 0
        for i in range(len(MAP) -1, -1, -1):
            if self._is_row_full(i):
                self._remove_row(i)
                self._move_figures(i)
                points += 1
        return points

    def _add_figure_status(self):
        """Adding stopped figure into position map

        When last moving figure stops, get all tiles positions and update it on
            position map.
        """
        figure_positions = self.figure.get_tiles_positions()
        for position in figure_positions:
            self.tiles_positions[position[1]][position[0]] = 1

    def _check_next_figure_move(self):
        """Check legality of next figure move

        Check figures should stop at next move and create new figure. Also
            skip figure is not exist yet in map.
        """
        figure_positions = self.figure.get_tiles_positions()

        for position in figure_positions:
            if self._is_figure_exist_in_board(position):
                return
            if self._is_figure_should_stop(position):
                self._add_figure_status()
                self.figures.append(self.figure)
                self.figure = Figure(self.display_surface)
                self.figure.build_figure()
                return

    def is_game_over(self):
        """Is game over

        Check any tile exist in first row.
        """
        for item in self.tiles_positions[0]:
            if item == 1:
                return True
        return False

    def _is_figure_exist_in_board(self, position):
        """Is figure is visible on the board

        Args:
            position: tuple(int, int), Represnt cordinate on postion map.
        """
        return position[1] < 0

    def _is_figure_should_stop(self, position):
        """Is figure should stop

        Check if tile moved to end of map or above other tile.

        Args:
            position: tuple(int, int), Represnt cordinate on postion map.

        """
        return position[1] == 18 or self.tiles_positions[position[1]+1][position[0]] == 1

    def _is_row_full(self, row):
        """Is row full

        Check if all positions in row are 1, then row is full.

        Args:
            row: int, Value represent cheking index row.
        """
        if row < 0:
            raise BaseException
        for postion in self.tiles_positions[row]:
            if postion == 0:
                return False
        return True

    def _remove_row(self, row):
        """Remove row

        Remove tiles and clear positions on map.

        Args:
            row: int, Value represent cheking index row.
        """
        positions = []
        for index in range(len(self.tiles_positions[-1])):
            position = [index, row]
            self.tiles_positions[position[1]][position[0]] = 0
            positions.append(position)
        for figure in self.figures:
            figure.remove_tiles_at_postions(positions)

    def _move_figures(self, row):
        """Move figures above row down

        Move all figures above row one column down.

        Args:
            row: int, Value represent cheking index row.
        """
        for figure in self.figures:
            figure.move_tiles_above_row(row)
        self.tiles_positions.pop(row)
        self.tiles_positions.insert(0, [0 ,0 ,0 ,0 ,0, 0, 0, 0, 0])
        