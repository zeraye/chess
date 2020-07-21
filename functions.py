# Importing libraries
from main import *
from board import *


# Selecting square
def select(row, col):
    if not board[row][col][0] == '':
        board[row][col][2] = True


# Checkig if any piece is selected
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
    return False


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


# Finding piece by type
def find_by_selected():
    i = 0
    j = 0
    while i < 8:
        while j < 8:
            if board[i][j][2]:
                return i, j
            j += 1
        j = 0
        i += 1


# Finding piece by row and col
def find_by_pos(row, col):
    if not board[row][col] == '':
        return board[row][col][0], board[row][col][1]


# Checing if move is possible and correct
def can_move(new_row, new_col, type, color, white_king_moved, black_king_moved):
    old_row, old_col = find_by_selected()
    if type == 'KING' and color == 1:
        if old_row == 7 and old_col == 4 and not white_king_moved:
            if find_by_pos(7, 3)[0] == '' and find_by_pos(7, 2)[0] == '' and find_by_pos(7, 1)[0] == '':
                if find_by_pos(7, 0)[0] == 'ROOK':
                    if new_row == 7 and new_col == 0:
                        return 'castling-white-left'
            elif find_by_pos(7, 5)[0] == '' and find_by_pos(7, 6)[0] == '':
                if find_by_pos(7, 7)[0] == 'ROOK':
                    if new_row == 7 and new_col == 7:
                        return 'castling-white-right'
            else:
                if not (old_row == new_row and old_col == new_col):
                    if not find_by_pos(new_row, new_col)[1] == color:
                        if abs(old_row - new_row) < 2 and abs(old_col - new_col) < 2:
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
        else:
            if not (old_row == new_row and old_col == new_col):
                if not find_by_pos(new_row, new_col)[1] == color:
                    if abs(old_row - new_row) < 2 and abs(old_col - new_col) < 2:
                        if not find_by_pos(new_row, new_col)[0] == '':
                            remove_by_pos(new_row, new_col)
                        return 'correct-move'
    if type == 'KING' and color == 2:
        if old_row == 0 and old_col == 4 and not black_king_moved:
            if find_by_pos(0, 3)[0] == '' and find_by_pos(0, 2)[0] == '' and find_by_pos(0, 1)[0] == '':
                if find_by_pos(0, 0)[0] == 'ROOK':
                    if new_row == 0 and new_col == 0:
                        return 'castling-black-left'
            elif find_by_pos(0, 5)[0] == '' and find_by_pos(0, 6)[0] == '':
                if find_by_pos(0, 7)[0] == 'ROOK':
                    if new_row == 0 and new_col == 7:
                        return 'castling-black-right'
            else:
                if not (old_row == new_row and old_col == new_col):
                    if not find_by_pos(new_row, new_col)[1] == color:
                        if abs(old_row - new_row) < 2 and abs(old_col - new_col) < 2:
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
        else:
            if not (old_row == new_row and old_col == new_col):
                if not find_by_pos(new_row, new_col)[1] == color:
                    if abs(old_row - new_row) < 2 and abs(old_col - new_col) < 2:
                        if not find_by_pos(new_row, new_col)[0] == '':
                            remove_by_pos(new_row, new_col)
                        return 'correct-move'
    elif type == 'PAWN' and color == 1:
        if not (old_row == new_row and old_col == new_col):
            if not find_by_pos(new_row, new_col)[1] == color:
                if find_by_pos(new_row, new_col)[1] == 2:
                    if (new_row == old_row - 1 and new_col == old_col - 1) or (new_row == old_row - 1 and new_col == old_col + 1) and not (old_row - new_row == 1 and old_col == new_col):
                        # remove_by_pos(new_row, new_col)
                        return 'correct-move'
                elif find_by_pos(new_row, new_col)[1] == 0:
                    if old_row == 6:
                        if new_col == old_col and old_row - new_row <= 2:
                            return 'correct-move'
                    else:
                        if new_col == old_col and old_row - new_row == 1:
                            return 'correct-move'
    elif type == 'PAWN' and color == 2:
        if not (old_row == new_row and old_col == new_col):
            if not find_by_pos(new_row, new_col)[1] == color:
                if find_by_pos(new_row, new_col)[1] == 1:
                    if (new_row == old_row + 1 and new_col == old_col - 1) or (new_row == old_row + 1 and new_col == old_col + 1) and not (new_row - old_row == 1 and old_col == new_col):
                        # remove_by_pos(new_row, new_col)
                        return 'correct-move'
                elif find_by_pos(new_row, new_col)[1] == 0:
                    if old_row == 1:
                        if new_col == old_col and new_row - old_row <= 2:
                            return 'correct-move'
                    else:
                        if new_col == old_col and old_row - new_row == -1:
                            return 'correct-move'
    elif type == 'ROOK':
        if not (old_row == new_row and old_col == new_col):
            if not find_by_pos(new_row, new_col)[1] == color:
                if new_col == old_col or new_row == old_row:
                    if new_col == old_col:
                        if new_row > old_row:
                            i = 1
                            while i < new_row - old_row:
                                if not find_by_pos(old_row + i, new_col)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                        if new_row < old_row:
                            i = 1
                            while i < old_row - new_row:
                                if not find_by_pos(new_row + i, new_col)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                    elif new_row == old_row:
                        if new_col > old_col:
                            i = 1
                            while i < new_col - old_col:
                                if not find_by_pos(new_row, old_col + i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                        if new_col < old_col:
                            i = 1
                            while i < old_col - new_col:
                                if not find_by_pos(new_row, new_col + i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
    elif type == 'BISHOP':
        if not (old_row == new_row and old_col == new_col):
            if not find_by_pos(new_row, new_col)[1] == color:
                if abs(new_col - old_col) == abs(new_row - old_row):
                    if new_col > old_col:
                        if new_row > old_row:
                            i = 1
                            while i < new_row - old_row:
                                if not find_by_pos(old_row + i, (old_col + i))[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                        if new_row < old_row:
                            i = 1
                            while i < old_row - new_row:
                                if not find_by_pos(old_row - i, old_col + i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                    elif new_col < old_col:
                        if new_row > old_row:
                            i = 1
                            while i < new_row - old_row:
                                if not find_by_pos(old_row + i, old_col - i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                        if new_row < old_row:
                            i = 1
                            while i < old_row - new_row:
                                if not find_by_pos(old_row - i, old_col - i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
    elif type == 'QUEEN':
        if not (old_row == new_row and old_col == new_col):
            if not find_by_pos(new_row, new_col)[1] == color:
                if new_col == old_col or new_row == old_row:
                    if new_col == old_col:
                        if new_row > old_row:
                            i = 1
                            while i < new_row - old_row:
                                if not find_by_pos(old_row + i, new_col)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                        if new_row < old_row:
                            i = 1
                            while i < old_row - new_row:
                                if not find_by_pos(new_row + i, new_col)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                    elif new_row == old_row:
                        if new_col > old_col:
                            i = 1
                            while i < new_col - old_col:
                                if not find_by_pos(new_row, old_col + i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                        if new_col < old_col:
                            i = 1
                            while i < old_col - new_col:
                                if not find_by_pos(new_row, new_col + i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                if abs(new_col - old_col) == abs(new_row - old_row):
                    if new_col > old_col:
                        if new_row > old_row:
                            i = 1
                            while i < new_row - old_row:
                                if not find_by_pos(old_row + i, (old_col + i))[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                        if new_row < old_row:
                            i = 1
                            while i < old_row - new_row:
                                if not find_by_pos(old_row - i, old_col + i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
                    elif new_col < old_col:
                        if new_row > old_row:
                            i = 1
                            while i < new_row - old_row:
                                if not find_by_pos(old_row + i, old_col - i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return True
                        if new_row < old_row:
                            i = 1
                            while i < old_row - new_row:
                                if not find_by_pos(old_row - i, old_col - i)[0] == '':
                                    deselect()
                                    print('Incorrect move')
                                    return 'uncorrect-move'
                                i += 1
                            if not find_by_pos(new_row, new_col)[0] == '':
                                remove_by_pos(new_row, new_col)
                            return 'correct-move'
    elif type == 'KNIGHT':
        if not (old_row == new_row and old_col == new_col):
            if not find_by_pos(new_row, new_col)[1] == color:
                if (new_row == old_row - 1 and new_col == old_col - 2) or \
                        (new_row == old_row + 1 and new_col == old_col - 2) or \
                        (new_row == old_row + 2 and new_col == old_col - 1) or \
                        (new_row == old_row + 2 and new_col == old_col + 1) or \
                        (new_row == old_row + 1 and new_col == old_col + 2) or \
                        (new_row == old_row - 1 and new_col == old_col + 2) or \
                        (new_row == old_row - 2 and new_col == old_col + 1) or \
                        (new_row == old_row - 2 and new_col == old_col - 1):
                    if not find_by_pos(new_row, new_col)[0] == '':
                        remove_by_pos(new_row, new_col)
                    return 'correct-move'
    print('Incorrect move')
    return 'uncorrect-move'


# Removing all pieces from board by type
def remove_by_type(type, color):
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


# Removing piece from board by row and col
def remove_by_pos(row, col):
    board[row][col][0] = ''
    board[row][col][1] = 0
    board[row][col][2] = False


# Getting row and col from clicked position
def get_clicked_pos(pos):
    x, y = pos
    row = y // 100
    col = x // 100
    return row, col
