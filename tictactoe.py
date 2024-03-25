"""
Tic Tac Toe Player
"""

import math

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
    # raise NotImplementedError

    # Initialize the count of non-empty pieces
    count  = 0

    # Count up the number of non-empty pieces
    for row in board:
        for element in row:
            if element is not EMPTY:
                print("not empty")
                count += 1

    # if the number of non-empty pieces is odd, like 1, then it is O's turn
    # else, if the number is even, like 0, or 2, it is X's turn
    if (count % 2 ) == 0:
        return X
    else:
        return y
    # raise NotImplementedError



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError

    # record the possible actions
    actions = set()

    # count the rows
    i = 0
    # count the columns
    j = 0

    # for row i
    for row in board:

        # column or element j in each row
        for column in i:

            # check if the element in row and column is empty
            if column is not EMPTY:

                # if the space is empty, record it as a possible move
                actions.append((i,j))

            # increase the column count
            j += 1

            # if we are at the end of the row, reset the column count, offsetting the zero starting index by 1
            if (j+1)%3 == 0:

                # reset the column count
                j = 0

        # after going through all the columns in a row, increase the row count by 1
        i += 1



    # return the actions
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    raise NotImplementedError

    # Decide who's move it is
    current_player = player(board)

    # i represents the row, the first element of the action tuple
    i = action[0]

    # j represents the colun, the second element of the action tuple
    j = action[1]

    # check to see whether the move is valid, ie that the space is empty
    if board[i][j] is not EMPTY:

        # Look at the action tuple (i, j) place, and change it to the current player's symbol
        board[i][j] = current_player
    else:
        raise RuntimeError('Invalid action')

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError
    # check for a row win
    for row in board:
        if (row[0] == row[1]) and (row[1] == row [2]):
            return row[0]

    # check for a column win
    row_max = range(3)
    for i in row_max:
        if (board[i][0] == board[i][0]) and (board[i][1] == board[i[2]]):
            return board[i][0]

    # check for a diagonal down to the right win
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        return true

    # check for a diagonal down to the left win
    if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
        return true

    return false


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError
    # check to see if there are any empty spaces in the board
    for row in board:
        for column in row:
            if board[row][column] is EMPTY:
                return false

    # raise NotImplementedError
    return true


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError
    # presume only called if termal(board) is true

    # Check the winner and return the expected output
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    # raise NotImplementedError
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
