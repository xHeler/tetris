import pygame

from src.utils.settings import WIDTH, HEIGHT
from src.utils.input import Input
from src.utils.button import Button


class Menu:
    def __init__(self):
        x = WIDTH/4
        y =  HEIGHT/3
        self.username = Input(x, y)
        self.password = Input(x, y + 100, True)
        self.button = Button("Log In", 150, 32, WIDTH/2, y + 200)
    
    def catch_events(self, event):
        self.username.catch_events(event)
        self.password.catch_events(event)
        self.button.catch_events(event)
                
    def update(self):    
        self.username.update()
        self.password.update()
        self.button.update()