from random import randint
from utils.settings import COLORS


class Color:
    color_id = 0  
    
    def __init__(self):
        self.colors = COLORS
        
    def get_color(self):
        index = Color.color_id % len(self.colors)
        print('index:', index)
        Color.color_id += 1
        return self.colors[index]