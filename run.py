from random import randint

#scores = {"computer": 0, "player": 0}



class gameBoard:
    """
    Main game board class. Sets the size of game board.....
    """

    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.action = []
        self.board = [[" " for x in range(3)] for y in range(3)]

    def display_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")


    

