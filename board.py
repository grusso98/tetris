import numpy as np
import pygame
from shape import generate_colours, generate_shapes
class Board:

    def __init__(self, screen, height=30, width=15):
        self.height = height
        self.width = width
        self.screen = screen
        self.matrix = np.zeros([width, height], dtype=int)
        self.current_tile = None
        self.score = 0
        self.colors = generate_colours()
        self.shapes = generate_shapes()
    
    def draw(self):
        blockSize = 35
        x_offset = 100
        y_offset = 50
        for x in range(0, self.width):
            for y in range (0, self.height):
                rect = pygame.Rect(x_offset + x * blockSize, y_offset + y * blockSize, blockSize, blockSize)
                pygame.draw.rect(self.screen, self.colors[self.matrix[x,y]], rect)