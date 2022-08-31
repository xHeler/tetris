import pygame


class Button:
    def __init__(self, text, width, height, x, y):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # font
        self.font = pygame.font.Font(None, 32)
        
        # create rectangle
        self.input_rect = pygame.Rect(0, 0, width, height)
        self.input_rect.center = (x, y)
        
        # colors
        self.background_color = pygame.Color('White')
        text_color = pygame.Color('black')
        
        # text surface        
        self.text_surface = self.font.render(text, True, text_color)

    def catch_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.background_color = pygame.Color('gray')
                return True
        return False
    
    def update(self):
        height = self.text_surface.get_height() / 2
        width = self.text_surface.get_width() / 2
        pygame.draw.rect(self.display_surface, self.background_color, self.input_rect)
        self.display_surface.blit(self.text_surface, (self.input_rect.center[0] - width, self.input_rect.center[1] - height))
