"""
Tic Tac Toe Player
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
    """
    Returns player who has the next turn on a board.
    """

    
    xcount = 0
    Ocount = 0
    emptycount = 0
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 'X':
                xcount+=1
            elif board[x][y] == 'O':
                Ocount+=1
            else:
                emptycount+=1
    if xcount == Ocount:
        return X
    else:
        return O
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    spacecounter = set()
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == None:
                spacecounter.add((x, y))
    
    return spacecounter


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
  #  print(action)
    x = action[0]
    y = action[1]
    board = copy.deepcopy(board)
    board[x][y] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(3):
        if board[x][0] == 'X' and board[x][1] == 'X' and board[x][2] == 'X':
            return X
        elif board[x][0] == 'O' and board[x][1] == 'O' and board[x][2] == 'O':
            return O
    for y in range(3):
        if board[0][y] == 'X' and board[1][y] == 'X' and board[2][y] == 'X':
            return X
        elif board[0][y] == 'O' and board[1][y] == 'O' and board[2][y] == 'O':
            return O
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return X
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return O
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return X
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif None not in board[0] and None not in board[1] and None not in board[2]:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    action = list(actions(board))
    turn = player(board)
    move = ()
   
    if turn == X:
        movevalue = -math.inf
        print("x")
        for actionstate in action:
            w = MIN_VALUE(result(board, actionstate))
            print(w)
            if w == 1:
                move = actionstate
                return move
            elif w > movevalue:
                movevalue = w
                move = actionstate

        return move
    else:
        movevalue = math.inf
        print("o")
        for actionstate in action:
            w = MAX_VALUE(result(board, actionstate))
            print(w)
            if w == -1:
                move = actionstate
                return move
            elif w < movevalue:
                movevalue = w
                move = actionstate

        return move
        
def MAX_VALUE(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    maxvalue = -math.inf
    action = list(actions(board))
    for actionstate in action:
        #print("max_value function")
       # print("before max:")
       # print(v)
        v = max(v, MIN_VALUE(result(board, actionstate)))
        if v == 1:
            return v
        maxvalue = max(v, maxvalue)
    return maxvalue 

def MIN_VALUE(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    minvalue = math.inf
    action = list(actions(board))
    for actionstate in action:
        #print("MIN VALUE FUNCTIOn")
        v = min(v, MAX_VALUE(result(board, actionstate)))
        if v == -1:
            return v
        minvalue = min(v, minvalue)
    return minvalue