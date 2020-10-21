import numpy as np
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, PIXEL_SIZE

class Grid:

    def __init__(self):
        self.grid = [[0 for _ in range(DISPLAY_WIDTH // PIXEL_SIZE)] for _ in range(DISPLAY_HEIGHT // PIXEL_SIZE)]

    def put_snake_on_grid(self, postion):
        index_y = postion[1] // PIXEL_SIZE
        index_x = postion[0] // PIXEL_SIZE
        self.grid[index_y][index_x] = 1

    def remove_snake_on_grid(self, postion):
        index_y = postion[1] // PIXEL_SIZE
        index_x = postion[0] // PIXEL_SIZE
        self.grid[index_y][index_x] = 0
