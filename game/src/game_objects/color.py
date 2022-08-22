# -*- coding: utf-8 -*-
"""Color

Roll random color from color list.
"""
from src.utils.settings import COLORS


class Color:
    """Color Class

    Attribiutes:
        colors: list, List with possible colors.
        color_id: int, Static value define color id.
    """
    color_id = 0

    def __init__(self):
        """Constructor

        Attribiutes:
            colors: list, List with possible colors.
        """
        self.colors = COLORS

    def get_next_color(self):
        """Get next color in order

        Return:
            color, str, Name of color.
        """
        index = Color.color_id % len(self.colors)
        Color.color_id += 1
        return self.colors[index]

    def get_color(self, color):
        """Get color

        Get color if exist.

        Args:
            color, str, Name of color.

        Return:
            color, str, Name of color.
        """
        for value in enumerate(self.colors):
            if value == color:
                return color
        return self.colors[0]
