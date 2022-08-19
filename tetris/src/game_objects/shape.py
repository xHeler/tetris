# -*- coding: utf-8 -*-
"""Figure shape

That class define figure shape from .csv files exist in shapes directory.
"""
from copy import deepcopy
from os import walk
from csv import reader
from random import choice


class Shape:
    """Shape class

    Read shape of figure from .csv file.

    Attribiutes:
        path, str, Path to directory with shape files.
        _positions, list, Positions get from shape file.
    """
    def __init__(self, path):
        """Constructor

        Collect possition from file.

        Attribiutes:
            path, str, Path to directory with shape files.
            _positions, list, Positions get from shape file.
        """
        self.path = path
        self._positions = []
        self.collect_shape_positions()

    def get_random_shape(self):
        """"Get random shape positions

        Get random shape from file.
        """
        positions = choice(self._positions)
        return deepcopy(positions)

    def get_shape_by_index(self, index):
        """Get postions of shape by index
        """
        return deepcopy(self._positions[index])

    def collect_shape_positions(self):
        """Collect shape positions

        Collect all shapes from file.
        """
        files = self._get_shapes_file_list()
        self._positions = []
        for file in files:
            self._positions.append(self._get_shape_positions(file))

    def _get_shapes_file_list(self):
        """Get list of shapes
        """
        shapes = []
        for _, __, figures_file in walk(self.path):
            for file in figures_file:
                full_path = self.path + "/" + file
                shapes.append(full_path)
        return shapes

    def _get_shape_positions(self, file):
        """Get shape position

        Args:
            file, str, Filename of shape.
        """
        positions = []
        symbols = self._read_from_file_names(file)

        for column, _ in enumerate(symbols):
            for row, __ in enumerate(symbols[column]):
                if symbols[column][row] == '#':
                    positions.append([row, -column - 1])
        return positions

    def _read_from_file_names(self, file):
        """Read symbols from file

        Args:
            file, str, Shape file name.
        """
        symbols = []
        with open(file, 'r', encoding='utf-8') as read_file:
            csv_read = reader(read_file)
            for row in csv_read:
                symbols.append(row)
        symbols.reverse()
        return symbols
