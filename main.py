# Importing libraries
import pygame
import math
from draw import *
from functions import *

# Window settings
WIDTH = 800
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

# Colors
WHITE = (238, 238, 210)
GREY = (128, 128, 128)
GREEN = (118, 150, 86)
RED = (255, 0, 0)


# Main function
def main(win):
    print_board()
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
            if is_selected()[0] == '':
                deselect()
                select(row, col)

            else:
                type = is_selected()[0]
                color = is_selected()[1]
                if can_move(row, col, type, color):
                    remove(type, color)
                    board[row][col][0] = type
                    board[row][col][1] = color
                    deselect()

            print_board()
            draw(win)

        if not pygame.mouse.get_pressed()[0]:
            pressed = False

    pygame.quit()


# Initialize main function
if __name__ == '__main__':
    main(WIN)
