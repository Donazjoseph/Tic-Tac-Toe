"""
Tic Tac Toe 
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    
    qtdx = 0
    qtdo = 0

   
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                qtdx += 1
            if board[i][j] == O:
                qtdo += 1

    if qtdx > qtdo:
        return O
    else:
        return X


def actions(board):
   
    possibil = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibil.add((i, j))

    return possibil


def result(board, action):
    result = copy.deepcopy(board)

    try:
        if result[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            
            result[action[0]][action[1]] = player(board)
            return result
   
    except IndexError:
        print('Position already filled')

def winner(board):
    
    for i in range(3):
       
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] != EMPTY:
                return board[i][0]

        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] != EMPTY:
                return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != EMPTY:
            return board[0][0]

    if board[2][0] == board[1][1] == board[0][2]:
        if board[0][2] != EMPTY:
            return board[0][2]

    return None


def terminal(board):
    

    if winner(board) != None:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False

    return True

def utility(board):
    if terminal(board):
      
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    
    if terminal(board):
        return None
    else:
        if player(board) == X:
            v_mini = float('-inf')
            for possibil in actions(board):
                i = valueMini(result(board, possibil))
                if i > v_mini:
                    v_mini = i
                    moviment = possibil
        else:
            v_maxi = float('inf')
            for possibil in actions(board):
                i = valueMaxi(result(board, possibil))
                if i < v_maxi:
                    v_maxi = i
                    moviment = possibil

    return moviment


def valueMini(board):
    if terminal(board):
        return utility(board)

    v_mini = float('inf')

    for possibil in actions(board):
        v_mini = min(v_mini, valueMaxi(result(board, possibil)))
        
    return v_mini


def valueMaxi(board):
    if terminal(board):
        return utility(board)

    v_maxi = float('-inf')

    for possibil in actions(board):
        v_maxi = max(v_maxi, valueMini(result(board, possibil)))

    return v_maxi
