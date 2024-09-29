import pygame.display
from board import Board

class Tetris:
    def __init__(self):
        self.screen =  pygame.display.set_mode((720,1280))
        self.board = Board(self.screen)
        self.running = True
        self.speed = 10
        self.clock = pygame.time.Clock()
        self.run()
    
    def run(self):
        while self.running == True:
            self.screen.fill("Black")
            pygame.display.flip()
            self.board.draw()
        pygame.quit()

Tetris().run()