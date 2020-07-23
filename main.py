# Importing libraries
import pygame
import math
import os
from draw import *
from functions import *
from board import *

# Window settings
WIDTH = 800
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF, 32)
pygame.display.set_caption('Chess')

# Colors
WHITE = (238, 238, 210)
GREY = (128, 128, 128)
GREEN = (118, 150, 86)
RED = (255, 0, 0)


# Main function
def main(win):
    white_king_moved = False
    black_king_moved = False
    white = True
    black = False
    run = True
    pressed = False
    draw(win)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    deselect()

        if pygame.mouse.get_pressed()[0] and not pressed:
            pressed = True
            row, col = get_clicked_pos(pygame.mouse.get_pos())
            if not is_selected():
                deselect()
                if find_by_pos(row, col)[1] == 1 and white:
                    select(row, col)
                elif find_by_pos(row, col)[1] == 2 and black:
                    select(row, col)
            else:
                type = is_selected()[0]
                color = is_selected()[1]
                if can_move(row, col, type, color, white_king_moved, black_king_moved) == 'uncorrect-move':
                    deselect()
                elif can_move(row, col, type, color, white_king_moved, black_king_moved) == 'correct-move':
                    remove_by_pos(find_by_selected()[0], find_by_selected()[1])
                    board[row][col][0] = type
                    board[row][col][1] = color
                    white = not white
                    black = not black
                    deselect()
                    if type == 'KING':
                        if color == 1:
                            white_king_moved = True
                        elif color == 2:
                            black_king_moved = True
                elif can_move(row, col, type, color, white_king_moved, black_king_moved) == 'castling-white-left':
                    board[7][0][0] = ''
                    board[7][0][1] = 0
                    board[7][4][0] = ''
                    board[7][4][1] = 0
                    board[7][3][0] = 'ROOK'
                    board[7][3][1] = 1
                    board[7][2][0] = 'KING'
                    board[7][2][1] = 1
                    white_king_moved = True
                    white = not white
                    black = not black
                    deselect()
                elif can_move(row, col, type, color, white_king_moved, black_king_moved) == 'castling-white-right':
                    board[7][7][0] = ''
                    board[7][7][1] = 0
                    board[7][4][0] = ''
                    board[7][4][1] = 0
                    board[7][5][0] = 'ROOK'
                    board[7][5][1] = 1
                    board[7][6][0] = 'KING'
                    board[7][6][1] = 1
                    white_king_moved = True
                    white = not white
                    black = not black
                    deselect()
                elif can_move(row, col, type, color, white_king_moved, black_king_moved) == 'castling-black-left':
                    board[0][0][0] = ''
                    board[0][0][1] = 0
                    board[0][4][0] = ''
                    board[0][4][1] = 0
                    board[0][3][0] = 'ROOK'
                    board[0][3][1] = 2
                    board[0][2][0] = 'KING'
                    board[0][2][1] = 2
                    black_king_moved = True
                    white = not white
                    black = not black
                    deselect()
                elif can_move(row, col, type, color, white_king_moved, black_king_moved) == 'castling-black-right':
                    board[0][7][0] = ''
                    board[0][7][1] = 0
                    board[0][4][0] = ''
                    board[0][4][1] = 0
                    board[0][5][0] = 'ROOK'
                    board[0][5][1] = 2
                    board[0][6][0] = 'KING'
                    board[0][6][1] = 2
                    black_king_moved = True
                    white = not white
                    black = not black
                    deselect()
            print_board()
            draw(win)
            if check_mate() != True:
                run = False
                pygame.quit()

        if not pygame.mouse.get_pressed()[0]:
            pressed = False

    pygame.quit()


# Initialize main function
if __name__ == '__main__':
    main(WIN)
