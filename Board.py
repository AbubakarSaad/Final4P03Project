import numpy as np

def copy_board(board):
    # copy board 
    new_board = np.copy(board)
    return new_board

class Board:

    def __init__(self, board):
        self.board = board
        # print(self.board)

    def move_up(self):
        # move the tile up if possible
        new_state = copy_board(self.board)
        # print("something herere", len(new_state))
        i, j = np.where(new_state == 0)

        # U: (i-1, j)
        # print(i[0], j[0])
        i = i[0]
        j = j[0]
        
        # need a check before to see if its out of bounds
        if i-1 >= 0 and j < len(new_state):
            temp = new_state[i-1][j]
            new_state[i-1][j] = 0
            new_state[i][j] = temp
            return Board(new_state)
        else: 
            return None

        # print(new_state)
        
    def move_down(self):
        # move the tile down if possible
        # D: (i+1, j)

        new_state = copy_board(self.board)
        i, j = np.where(new_state == 0)

        # print(i[0], j[0])

        i = i[0]
        j = j[0]

         # need a check before to see if its out of bounds
        if i+1 < len(new_state) and j < len(new_state):
            temp = new_state[i+1][j]
            new_state[i+1][j] = 0
            new_state[i][j] = temp

            return Board(new_state)
        else:
            return None
        # print(new_state)
       


    def move_right(self):
        # move the tile right if possible
        # R: (i, j+1)

        new_state = copy_board(self.board)
        i, j = np.where(new_state == 0)

        # print(i[0], j[0])

        i = i[0]
        j = j[0]

         # need a check before to see if its out of bounds
        if i < len(new_state) and j+1 < len(new_state):
            temp = new_state[i][j+1]
            new_state[i][j+1] = 0
            new_state[i][j] = temp
            return Board(new_state)
        else:
            return None
        # print(new_state)
        
    
    def move_left(self):
        # move the tile left if possible
        # L: (i, j-1)
        new_state = copy_board(self.board)
        i, j = np.where(new_state == 0)

        # print(i[0], j[0])

        i = i[0]
        j = j[0]


         # need a check before to see if its out of bounds
        if i < len(new_state) and j-1 >= 0:
            temp = new_state[i][j-1]
            new_state[i][j-1] = 0
            new_state[i][j] = temp
            return Board(new_state)

        else:
            None
        # print(new_state)
        
    def print_board(self):
        return self.board

    def get_board(self):
        new_state = copy_board(self.board)
        return new_state