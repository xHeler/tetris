from random import randint
from utils.settings import COLORS


class Color:
    def __init__(self):
        self.color_id = 0   
        self.colors = COLORS
        
    def get_color(self):
        index = self.color_id % len(self.colors)
        self.color_id += 1
        return self.colors[index]