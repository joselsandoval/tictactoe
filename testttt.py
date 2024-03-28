import pygame
import sys
import time

import tictactoe as ttt
import util

board = ttt.semi_near_terminal_state()

print(f"\n Current board: {board} \n")

print(ttt.minimax(board))