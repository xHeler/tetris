import pygame


class Input:
    def __init__(self, x, y, password=False, border=6):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # font
        self.font = pygame.font.Font(None, 32)
        
        # password
        self.password = password
        
        # input text
        self.user_text = ''
        
        # create rectangle
        self.input_rect = pygame.Rect(x, y, x * 2, 32)
        self.border_rect =  pygame.Rect(
            x - border/2, y - border/2, 
            x*2 + border, 32 + border
        )
        
        # colors
        self.color = pygame.Color('red')
        self.border_color = pygame.Color('white')
        
        self.active = False
        
    def catch_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
                
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif len(self.user_text) < 15:
                self.user_text += event.unicode
                
    def update(self):
        if self.password:
            text_length = len(self.user_text)
            text_surface = self.font.render('*' * text_length, True, (255, 255, 255))
        else:
            text_surface = self.font.render(self.user_text, True, (255, 255, 255))
        if self.active:
            pygame.draw.rect(self.display_surface, pygame.Color('white'), self.border_rect)
        pygame.draw.rect(self.display_surface, self.color, self.input_rect)
        
        self.display_surface.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        