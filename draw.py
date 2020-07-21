# Importing libraries
from main import *

# Importing images
king_white_img = pygame.image.load(os.path.join(os.getcwd(), './img/king-white.png')).convert_alpha()
king_black_img = pygame.image.load(os.path.join(os.getcwd(), './img/king-black.png')).convert_alpha()
pawn_white_img = pygame.image.load(os.path.join(os.getcwd(), './img/pawn-white.png')).convert_alpha()
pawn_black_img = pygame.image.load(os.path.join(os.getcwd(), './img/pawn-black.png')).convert_alpha()
rook_white_img = pygame.image.load(os.path.join(os.getcwd(), './img/rook-white.png')).convert_alpha()
rook_black_img = pygame.image.load(os.path.join(os.getcwd(), './img/rook-black.png')).convert_alpha()
bishop_white_img = pygame.image.load(os.path.join(os.getcwd(), './img/bishop-white.png')).convert_alpha()
bishop_black_img = pygame.image.load(os.path.join(os.getcwd(), './img/bishop-black.png')).convert_alpha()
knight_white_img = pygame.image.load(os.path.join(os.getcwd(), './img/knight-white.png')).convert_alpha()
knight_black_img = pygame.image.load(os.path.join(os.getcwd(), './img/knight-black.png')).convert_alpha()
queen_white_img = pygame.image.load(os.path.join(os.getcwd(), './img/queen-white.png')).convert_alpha()
queen_black_img = pygame.image.load(os.path.join(os.getcwd(), './img/queen-black.png')).convert_alpha()


# Drawing pieces
def draw_pieces(win):
    i = 0
    j = 0
    while i < 8:
        while j < 8:
            if board[i][j][1] == 1:
                if board[i][j][0] == 'KING':
                    win.blit(king_white_img, (j * 100, i * 100))
                elif board[i][j][0] == 'PAWN':
                    win.blit(pawn_white_img, (j * 100, i * 100))
                elif board[i][j][0] == 'ROOK':
                    win.blit(rook_white_img, (j * 100, i * 100))
                elif board[i][j][0] == 'BISHOP':
                    win.blit(bishop_white_img, (j * 100, i * 100))
                elif board[i][j][0] == 'KNIGHT':
                    win.blit(knight_white_img, (j * 100, i * 100))
                elif board[i][j][0] == 'QUEEN':
                    win.blit(queen_white_img, (j * 100, i * 100))
            elif board[i][j][1] == 2:
                if board[i][j][0] == 'KING':
                    win.blit(king_black_img, (j * 100, i * 100))
                elif board[i][j][0] == 'PAWN':
                    win.blit(pawn_black_img, (j * 100, i * 100))
                elif board[i][j][0] == 'ROOK':
                    win.blit(rook_black_img, (j * 100, i * 100))
                elif board[i][j][0] == 'BISHOP':
                    win.blit(bishop_black_img, (j * 100, i * 100))
                elif board[i][j][0] == 'KNIGHT':
                    win.blit(knight_black_img, (j * 100, i * 100))
                elif board[i][j][0] == 'QUEEN':
                    win.blit(queen_black_img, (j * 100, i * 100))

            j += 1
        j = 0
        i += 1


# Coloring selected square to red
def draw_selected(win):
    try:
        empty_rect = pygame.Rect(find_by_selected()[1] * 100, find_by_selected()[0] * 100, 100, 100)
        pygame.draw.rect(win, (255, 0, 0), empty_rect, 1)
    except TypeError:
        print('ERROR with coloring selected rect')


# Drawing grid
def draw_grid(win):
    rows = 8
    cols = 8
    while rows > 0:
        while cols > 0:
            if (rows % 2 == 0 and cols % 2 == 0) or (rows % 2 != 0 and cols % 2 != 0):
                pygame.draw.rect(win, WHITE, ((rows - 1) * 100, (cols - 1) * 100, 100, 100))
            else:
                pygame.draw.rect(win, GREEN, ((rows - 1) * 100, (cols - 1) * 100, 100, 100))
            cols -= 1
        cols = 8
        rows -= 1
    rows -= 1


# Main drawing function
def draw(win):
    draw_grid(win)
    draw_selected(win)
    draw_pieces(win)
    pygame.display.update()


# Priting board to console
def print_board():
    print('\n')
    print('DRAWING BOARD')
    i = 0
    while i < len(board):
        print(board[i])
        i += 1
