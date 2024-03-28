import pygame
import sys
import time

import tictactoe as ttt
import util

board = ttt.o_for_win()

print(f"\n Current board: {board} \n")

print(ttt.minimax(board))