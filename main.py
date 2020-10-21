import time
import random
import init
import pygame
import numpy as np
from snake import Snake
from food import Food
from grid import Grid
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, PIXEL_SIZE, WHITE, FPS


game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('The Ultimate Snake')
clock = pygame.time.Clock()

def game_loop():

    snake = Snake()
    food = Food()
    grid = Grid()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(WHITE)
        
        food.draw(game_display)
        snake.draw(game_display)
        snake.move(grid, food, game_display)
        
        pygame.display.update()
        clock.tick(FPS)
    
if __name__ == "__main__":
    game_loop()
    pygame.quit()
    quit()