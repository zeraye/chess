# Importing libraries
from board import *


# Selecting square
def select(row, col):
    if not board[row][col][0] == '':
        board[row][col][2] = True


# Checkig if square is selected
def is_selected():
    i = 0
    j = 0
    while i < 8:
        while j < 8:
            if board[i][j][2]:
                return board[i][j][0], board[i][j][1]
            j += 1
        j = 0
        i += 1
    return '', 0


# Deselecting square
def deselect():
    i = 0
    j = 0
    while i < 8:
        while j < 8:
            board[i][j][2] = False
            j += 1
        j = 0
        i += 1


# Finding piece by type and color
def find_by_piece(type, color):
    i = 0
    j = 0
    while i < 8:
        while j < 8:
            if board[i][j][0] == type and board[i][j][1] == color:
                return i, j
            j += 1
        j = 0
        i += 1


# Finding piece by row and col
def find_by_place(row, col):
    if not board[row][col] == '':
        return board[row][col][0], board[row][col][1]


# Checing if move is possible and correct
def can_move(new_row, new_col, type, color):
    old_row, old_col = find_by_piece(type, color)
    # TODO: Write for every piece (bishop, knight, queen, rook)
    if type == 'KING':
        if not (old_row == new_row and old_col == new_col):
            if not find_by_place(new_row, new_col)[1] == color:
                if abs(old_row - new_row) < 2 and abs(old_col - new_col) < 2:
                    if not find_by_place(new_row, new_col) == '':
                        remove(find_by_place(new_row, new_col)[0], find_by_place(new_row, new_col)[1])
                    return True
    elif type == 'PAWN' and color == 1:
        if not (old_row == new_row and old_col == new_col):
            if not find_by_place(new_row, new_col)[1] == color:
                if find_by_place(new_row, new_col)[1] == 2:
                    if (old_row - new_row) < 2 and abs(old_col - new_col) < 2 and old_row > new_row:
                        remove(find_by_place(new_row, new_col)[0], find_by_place(new_row, new_col)[1])
                        return True
                elif find_by_place(new_row, new_col)[1] == 0:
                    if new_col == old_col and old_row - new_row == 1:
                        return True
    elif type == 'PAWN' and color == 2:
        if not (old_row == new_row and old_col == new_col):
            if not find_by_place(new_row, new_col)[1] == color:
                if find_by_place(new_row, new_col)[1] == 1:
                    if (old_row - new_row) < 2 and abs(old_col - new_col) < 2 and old_row < new_row:
                        remove(find_by_place(new_row, new_col)[0], find_by_place(new_row, new_col)[1])
                        return True
                elif find_by_place(new_row, new_col)[1] == 0:
                    if new_col == old_col and old_row - new_row == -1:
                        return True
    elif type == 'ROOK':
        if not (old_row == new_row and old_col == new_col):
            if not find_by_place(new_row, new_col)[1] == color:
                if new_col == old_col or new_row == old_row:
                    if True:  # TODO: Remove jumping over pieces
                        if not find_by_place(new_row, new_col) == '':
                            remove(find_by_place(new_row, new_col)[0], find_by_place(new_row, new_col)[1])
                        return True
    print('Incorrect move')
    return False


# Removing piece from board
def remove(type, color):
    i = 0
    j = 0
    while i < 8:
        while j < 8:
            if board[i][j][0] == type and board[i][j][1] == color:
                board[i][j][0] = ''
                board[i][j][1] = 0
            j += 1
        j = 0
        i += 1


# Getting row and col from clicked position
def get_clicked_pos(pos):
    x, y = pos
    row = y // 100
    col = x // 100
    return row, col
