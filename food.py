import pygame
import random

from constants import *

class Food:

    def __init__(self):
        self.x = round(random.randrange(1, DISPLAY_WIDTH - PIXEL_SIZE) / 20.0) * 20
        self.y = round(random.randrange(1, DISPLAY_HEIGHT - PIXEL_SIZE) / 20.0) * 20

    def draw(self, game_display):
        pygame.draw.rect(game_display, RED, [self.x, self.y, PIXEL_SIZE, PIXEL_SIZE])

    def update(self):
        self.x = round(random.randrange(0, DISPLAY_WIDTH - PIXEL_SIZE) / 20.0) * 20
        self.y = round(random.randrange(0, DISPLAY_HEIGHT - PIXEL_SIZE) / 20.0) * 20