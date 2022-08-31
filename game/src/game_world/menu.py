import pygame

from src.utils.settings import WIDTH, HEIGHT
from src.game_objects.input import Input
from src.game_objects.button import Button
from src.utils.network import connect_to_server



class Menu:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        
        x = WIDTH/4
        y =  HEIGHT/3
        
        self.email = Input(x, y)
        self.password = Input(x, y + 75, True)
        self.button = Button("Log In", 150, 32, WIDTH/2, y + 150)
        
        self.connection_status = False
        
        # Text
        self.font = pygame.font.Font(None, 45)
        self.font_small = pygame.font.Font(None, 26)
        
        self.text_surface = self.font.render("Witamy Samuraju", False, (255, 255, 255))
        height = self.text_surface.get_height() / 2
        width = self.text_surface.get_width() / 2
        self.text_cordinates = (WIDTH/2 - width, y - 75)
        
        # Text error
        self.text_error_surface = self.font_small.render("", False, (255, 0, 0))
        self.text_error_cordinates = (WIDTH/2 - width - 50, y - 40)

    
    def catch_events(self, event):
        self.email.catch_events(event)
        self.password.catch_events(event)
        if self.button.is_button_pressed(event):
            self.connection_status, self.errors = connect_to_server(
                self.email.user_text, 
                self.password.user_text
                )
            self.button.change_button_color()
            self.text_error_surface = self.font_small.render(str(self.errors), False, (255, 0, 0))
                
    def update(self):    
        self.email.update()
        self.password.update()
        self.button.update()
        
        self.display_surface.blit(self.text_surface, self.text_cordinates)
        self.display_surface.blit(self.text_error_surface, self.text_error_cordinates)