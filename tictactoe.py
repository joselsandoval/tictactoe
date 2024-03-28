"""
Tic Tac Toe Player
"""
import math

class Node():
    def __init__(self, state, parent, action, weight):
        self.state = state
        self.parent = parent
        self.action = action
        self.weight = weight


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


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

def near_terminal_state():
    """
    Returns a test state of the board that is near terminal.
    """
    return[[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, X],
            [EMPTY, EMPTY, O]]

def semi_near_terminal_state():
    """
    Returns a test state of the board that is near terminal.
    """
    return[[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, X],
            [EMPTY, O, O]]


def o_for_win():
    """
    Returns a test state of the board that is near terminal.
    """
    return[[X, X, EMPTY],
            [O, X, X],
            [EMPTY, O, O]]

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
                count += 1

    # if the number of non-empty pieces is odd, like 1, then it is O's turn
    # else, if the number is even, like 0, or 2, it is X's turn
    if (count % 2 ) == 0:
        return X
    else:
        return O
    # raise NotImplementedError



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError

    # record the possible actions
    actions = set()

    # for row i
    for i in range(3):

        # column or element j in each row
        for j in range(3):

            # check if the element in row and column is empty
            if board[i][j] is EMPTY:

                # if the space is empty, record it as a possible move
                actions.add((i,j))

    # return the actions
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Decide who's move it is
    current_player = player(board)

    # i represents the row, the first element of the action tuple
    i = action[0]

    # j represents the colun, the second element of the action tuple
    j = action[1]

    # check to see whether the move is valid, ie that the space is empty
    if board[i][j] == EMPTY:

        # Look at the action tuple (i, j) place, and change it to the current player's symbol
        board[i][j] = current_player

    else:
        raise RuntimeError('Invalid action')

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    winner = None

    # check for a row win
    for i in range(3):
        if (board[i][0] is not EMPTY) and (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]):
            # print("row win")
            winner = board[i][0]
            # return board[i][0]

    # for row in board:
        # if (row[0] is not EMPTY) and (row[0] == row[1]) and (row[1] == row [2]):
            # print("Row win")
            # return row[0]

    # check for a column win
    for j in range(3):
        if (board[0][j] is not EMPTY) and (board[0][j] == board[1][j]) and (board[1][j] == board[2][j]):
            # print("Column win")
            winner = board[0][j]
            # return board[0][j]

    # check for a diagonal down to the right win
    if (board[1][1] is not EMPTY) and (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        # print("Diag to right win")
        winner = board[1][1]
        # return board[1][1]

    # check for a diagonal down to the left win
    if (board[1][1] is not EMPTY) and (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
        # print("Diag to left win")
        winner = board[1][1]
        # return board[1][1]

    # return None
    # print(winner)
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check if there is a winner to the game
    if winner(board) is None:
        # check to see if there are any empty spaces in the board
        for i in range(3):
        # for row in board:
            for j in range(3):
                if (board[i][j] == EMPTY):
                # if (row[j] == "EMPTY"):
                    return False

    #for row in board:
        #for column in row:
            #if board[row][column] == EMPTY:
                #return false

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
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
    
    # if the board is a terminal board, the minimax function should return None
    if terminal(board) is True:
        # return utility(board)
        return None

    # for each possible action, there is a maximum to the minimax function.  Let's save the action and minimax reward value
    history_list = set()

    
    # determine the curren player
    current_player = player(board) 

    if current_player == X:
        initial_weight = -2
    else:
        initial_weight = 2

    # build a tree that represents the game state and all possible other states
    tree = QueueFrontier()

    # make an adjancy matrix
    adj = []

    # Initialize the frontier to just the starting position
    start = Node(state=board, parent=None, action=None, weight=None)
    frontier = QueueFrontier()
    # frontier = StackFrontier()
    frontier.add(start)
    tree.add(start)

    # print(start.parent)
    # Keep track of the explored states
    explored = []

    num_explored = 0

    # initialize the best value and best action
    best_value = 0
    best_action = (-1, -1)
        
    if current_player == X:
        best_value = -2
    else:
        best_value = 2

    while not frontier.empty():
        # pull off the current node on the frontier
        node = frontier.remove()
        # print(f"Now exploring board on the frontier: {node.state}")
        num_explored += 1
        explored.append(node.state)

        # get the actions for the current board
        # current_actions = actions(board)
        current_actions = actions(node.state)

        # enumerated_actions = print_actions(actions)
        # print(f"Actions for {board} board: {enumerated_actions}")
 
        for action in current_actions:
            # make a copy of the board
            # copy_board = clone_board(board)
            copy_board = clone_board(node.state)

            # apply the result (then return the minimax fuction for that board)
            copy_board = result(copy_board, action)

            # Check to see if we have explored this state, now we have the resulting board from the action
            if copy_board not in explored:

                print(f"{copy_board} not in Explored: {explored}")

                # if the action you are choosing results in a terminal board and that board beats my current best option, then record the action that resulted in that board
                if terminal(copy_board):
            
                    # print(f"Terminal board found in one move from board {board} with the action {action} and it is {copy_board}")
                    # print(f"Terminal board found in one move from board {node.state} with the action {action} by player {player(node.state)} and it is {copy_board}")

                    # best_board = initial_state()

                    current_value = utility(copy_board)

                    # print(f"Current value of Terminal board, {current_value}")

                    # if we are X, trying to maximize our score and we get a better value
                    if (current_player == X) and (current_value > best_value):
                
                        # print(f"Player {current_player}, Action better: {action} with utility {current_value} than {best_action}")

                        # save the action that resulted in the best board and save the best value associated with it
                        best_action = action
                        # print(f"Better action is: {best_action}")
                        best_value = current_value

                    elif (current_player == O) and (current_value < best_value):
                
                        # print(f"Player {current_player}, Action better: {action} than {best_action}")

                        # print(action)

                        # save the action that resulted in the best board and save the best value associated with it
                        best_action = action
                        # print(f"Better action is: {best_action}")

                        best_value = current_value
            
                    current_weight = utility(copy_board)
                    current_node = Node(state=copy_board, parent=board, action=action, weight=current_weight)
                    # adj[node.state].append[copy_board]
                    # adj[copy_board].append[node.state]
        
                # if our action does not result in a terminal board, we need to recursively call the minimax function
                else:
                    current_weight = None
                    # Create a node to the frontier to be explored
                    current_node = Node(state=copy_board, parent=board, action=action, weight=current_weight)
                    # add the current node to the frontier to be explored
                    frontier.add(current_node)
                    # return the value of the minimax function for the particular board and save it in a tuple
                    # return minimax(copy_board)
        
                # each action is a node with parent start
                # make a node for each action and add it to the frontier
                
                tree.add(current_node)

    # return the best action
    return best_action

def print_actions(board):
    enumerated_actions = ""
    
    action_count = 0
    
    # get the actions for the current board
    current_actions = actions(board)

    for action in current_actions:
        item_count = 0
        

        action_str = ""
        
        if action_count != 0:
            action_str += " "

        action_str += "("

        for item in action:
            if item_count != 0:
                action_str += ","
            action_str = action_str + str(item)
            item_count += 1

        action_str += ")"

        enumerated_actions += action_str
        action_count += 1

    return enumerated_actions

def minimax_with_value(board):
    # determines the highest score for a given branch of a decision tree
    actionsValues = set()

    # if the board is a terminal board, the minimax function should return None
    if terminal(board) is True:
        # return utility(board)
        return None

    # determine the curren player
    current_player = player(board) 

    # initialize the best value and best action
    best_value = 0
    best_action = (-1, -1)

    if current_player == X:
        best_value = -2
    else:
        best_value = 2

    for action in actions(board):
        print(f"Terminal board found in one move to be, {board}")

        # print(action)

        # make a copy of the board
        copy_board = clone_board(board)

        # apply the result then return the minimax fuction for that board
        copy_board = result(copy_board, action)


        # if the action you are choosing results in a terminal board and that board beats my current best option, then record the action that resulted in that board
        if terminal(copy_board):
            
            print(f"Terminal board found from board {board} and it is {copy_board}")

            # best_board = initial_state()

            current_value = utility(copy_board)

            print(f"Current value of Terminal board, {current_value}")

            # if we are X, trying to maximize our score and we get a better value
            if (current_player == X) and (current_value > best_value):
                
                print(f"Player X, Action better: {action} with utility {current_value} than {best_action}")

                # save the action that resulted in the best board and save the best value associated with it
                best_action = action
                print(f"Better action is: {best_action}")
                best_value = current_value

            elif (current_player == O) and (current_value < best_value):
                
                print(f"Player O, Action better: {action} than {best_action}")

                # print(action)

                # save the action that resulted in the best board and save the best value associated with it
                best_action = action
                print(f"Better action is: {best_action}")

                best_value = current_value
            
            actionsValues.add((best_action, best_value))        
            
        # if our action does not result in a terminal board, we need to recursively call the minimax function
        else:
            # return the value of the minimax function for the particular board and save it in a tuple
            latest_actionsValues= minimax_with_value(copy_board)
            if latest_actionsValues is not None:
                actionsValues.update(latest_actionsValues) 

    # go through all the actions and values gathered to find out which one is rated the best

    return actionsValues


def clone_board(board):
    
    new_board = initial_state()

    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]
    
    return new_board
