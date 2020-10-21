import pygame
import numpy as np
import random
import copy

from astar import *
from constants import *

class Snake:

    def __init__(self):
        self.x = round(random.randrange(0, DISPLAY_WIDTH - PIXEL_SIZE) / 20.0) * 20
        self.y = round(random.randrange(0, DISPLAY_HEIGHT - PIXEL_SIZE) / 20.0) * 20
        self.snake_body = [[self.x, self.y]]
        self.prev = [[self.x, self.y]]
        self.snake_len = 1
        self.speed_x = 0
        self.speed_y = 0
        self.eaten = True
        self.path = []
        
    def draw(self, game_display):
        l = 0
        for snake in self.snake_body:
            if(l == len(self.snake_body) - 1):
                pygame.draw.rect(game_display, BLUE, [snake[0], snake[1], PIXEL_SIZE, PIXEL_SIZE])
            else:
                pygame.draw.rect(game_display,  BLACK, [snake[0], snake[1], PIXEL_SIZE, PIXEL_SIZE])
                l += 1

    def eat(self, apple_x, apple_y):    
        if(self.x == apple_x and self.y == apple_y):
            self.eaten = True
            self.snake_len += 1
            self.score += 1
            return True
        return False

    def dead(self):
        if self.x >= DISPLAY_WIDTH or self.x <= 0 or self.y >= DISPLAY_HEIGHT or self.y <= 0:
            print('Snake killed! Rip! Score is {}'.format(self.score))
            self.eaten = True
            return True
        
        for each in self.snake_body[:-1]:
            if each == self.snake_body[-1]:
                print('OOf')
                self.eaten = True
                return True

        return False

    def update(self):
        snakehead = []
        snakehead.append(self.x)
        snakehead.append(self.y)

        self.snake_body.append(snakehead)

        if len(self.snake_body) > self.snake_len:
            del self.snake_body[0]
            
    def move(self, grid, food, game_display):
        if(len(self.path) == 0 and self.eaten == False):
            self.snake_len += 1
            for body in self.prev:
                grid.remove_snake_on_grid(body)
            self.prev = []
            self.update()
            food.update()
            food.draw(game_display)
            self.eaten = True

        if(self.eaten):
            self.eaten = False
            for body in self.snake_body:
                grid.put_snake_on_grid(body)

            self.prev = copy.deepcopy(self.snake_body)
            self.path = astar(grid.grid, (self.x // PIXEL_SIZE, self.y // PIXEL_SIZE), (food.x // PIXEL_SIZE, food.y // PIXEL_SIZE))

        self.speed_x = 0
        self.speed_y = 0

        if(self.path[0][0] * PIXEL_SIZE < self.x):
            self.speed_x = - PIXEL_SIZE
        elif(self.path[0][0] * PIXEL_SIZE > self.x):
            self.speed_x = PIXEL_SIZE

        if(self.path[0][1] * PIXEL_SIZE > self.y):
            self.speed_y =  PIXEL_SIZE
        elif(self.path[0][1] * PIXEL_SIZE < self.y):
            self.speed_y = - PIXEL_SIZE

        self.x += self.speed_x
        self.y += self.speed_y
        self.update()
        self.path.pop(0)