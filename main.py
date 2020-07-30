import sys, os
import pygame
from pygame.locals import *
import engine

pygame.init()

win_wt, win_ht = (9*16*4), (11*16*4)
fps_clock = pygame.time.Clock()
fps = 60

win = pygame.display.set_mode((win_wt, win_ht))
number_font = pygame.font.Font(os.path.join("assets", "font.ttf"), 20)

def terminate():
    pygame.quit()
    sys.exit()


def out_events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            terminate()

def print_text(font, text, x, y):
    win.blit(font.render(str(text), True, (0, 0, 0)), (x, y))
    pass



class Board(object):

    def __init__(self, board):
        self.board = board

    def draw(self, win):

        for i in range(0, 10):

            # horizontal lines
            if (i % 3) == 0:
                pygame.draw.line(win, (0, 0, 0), (45, 64 + 45 + (i * 54)),
                                 (win_wt - 45, 64 + 45 + (i * 54)), 2)
                
                pygame.draw.line(win, (0, 0, 0), (45 + (i * 54),
                                                  64 + 45), (45 + (i * 54), win_ht - 64 - 45), 2)
            else:
                pygame.draw.line(win, (0, 0, 0), (45, 64 + 45 + (i * 54)),
                                 (win_wt - 45, 64 + 45 + (i * 54)), 1)

            # vertical lines
                pygame.draw.line(win, (0, 0, 0), (45 + (i * 54),
                                                64 + 45), (45 + (i * 54), win_ht - 64 - 45))
            pass
        
        for row in range(0, 9):
            for col in range(0, 9):
                if self.board[row][col] != 0:
                    print_text(number_font, self.board[row][col], row*54 + 45 + 27 - 10, col*54 + 54 + 45 + 27)
                pass
            pass
        
        pass


def main():

    grid = engine.generate_grid(15)
    engine.print_grid(grid)

    def run_game():

        board = Board(grid)
        
        while True:
            out_events()
            win.fill((86, 123, 121))

            board.draw(win)
            dt = fps_clock.tick(fps) / 1000
            dt *= 60

            pygame.display.update()

    while True:
        run_game()
        pass


if __name__ == "__main__":
    main()

