import numpy as np

class Board:

    def __init__(self, screen, height=30, width=15):
        self.height = height
        self.width = width
        self.screen = screen
        self.matrix = np.zeros([width, height], dtype=int)
        self.current_tile = None
        self.score = 0