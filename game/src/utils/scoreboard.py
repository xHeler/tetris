# -*- coding: utf-8 -*-
""" Scoreboard

Scoreboard draw actual player score.
"""
import os.path

import pygame

from src.utils.settings import FONT_PATH


class Scoreboard:
  """Class Scoreboard

  Attributes:
    display_surface: Surface, Main screen surface where all objects will
      be displayed.
    font: Font, Font class made by path to font file .ttf extension and
      font size.
  """

  def __init__(self, font_size=16, path=FONT_PATH):
    """Constructor

    Set origin display surface and made font object. Get path to font from
      settings file.

    Attributes:
      display_surface (Surface): Main screen surface where all objects will
        be displayed.
      font (Font): Font class made by path to font file .ttf extension and font
        size.
    """
    self.display_surface = pygame.display.get_surface()

    self.font_size = font_size
    self.font = pygame.font.Font(path, self.font_size)

  def draw(self, info):
    """Draw scoreboard at display

    Make text surface and draw it on display surface.
    """
    text_surface = self.font.render(str(info), False, (255, 255, 255))
    self.display_surface.blit(text_surface, (295, 62))

  def change_font(self, font_path):
    """ Change font type

    An argument font_path mean path to .ttf file.
    """
    if not os.path.exists(font_path):
      raise FileExistsError
    self.font = pygame.font.Font(font_path, self.font_size)
