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

    def display_board(self):
        """
        Display the game board to the user.
        """
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def user_input(self):
        """
        This takes user input, try which will raise ValueError if range is outside 1-9,
        raise ValueError if input are not integers. It will add the symbol to the display board method.
        """
        while True:
            try:
                guess = int(input("Please enter a number between 1-9:\n")) - 1
                if guess < MIN_BOARD_SIZE or guess > MAX_BOARD_SIZE:
                    raise ValueError(
                        "Please Enter a number between 1-9"
                    )
            except ValueError as e:
                print(f"Invalid Input: Please Enter a number between 1-9 , please try again.")
                self.user_input()
                return False
            
            if  self._check_occupied(guess):
                print("The place is occupied please choose another!")
                continue

            self.board[guess] = USER_SYMBOL
            print(f"You guess is: {guess + 1}")
            return True

    def computer_input(self):
        """
        This takes computer input, It will add the symbol to the display board method.
        """
        if self._board_full() or self.game_over:
            return
        
        while True:
            computer_move = random.randint(0, 8)
            if self._check_occupied(computer_move):
                continue

            self.board[computer_move] = COMPUTER_SYMBOL
            print(f"Computer guess is: {computer_move + 1}")
            return True

    def _check_occupied(self, index):
        """
        Checks if the symbol has occupied the space or not.
        """
        return self.board[index] in (USER_SYMBOL, COMPUTER_SYMBOL)



