#import random library
import random

#Defined global variables
MAX_BOARD_DIMENSION = 3
MAX_BOARD_SIZE = MAX_BOARD_DIMENSION * MAX_BOARD_DIMENSION - 1
MIN_BOARD_SIZE = 0

USER_SYMBOL = "X"
COMPUTER_SYMBOL = "O"



class TicTacToe:
    """
    Main TicTacToe class. Display game board, takes usser and computer input, check the position of the input, tells user who the winner is.
    """
    def __init__(self, name):
        self.name = name
        self.board = [location for location in range(1,10)]
        self.winner = None
        self.game_over = False
        self.computer = "Computer"


