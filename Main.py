import numpy as np
import Board
import Algorithms

# the solved state of the puzzle will be 
    # [[1,2,3], 
    #  [4,5,6],
    #  [7,8,0]]

# add a generator then shuffle it
# add a check for n-puzzle: done1

    
goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])


# start_state = Board.Board(np.array([[1,8,2], [0,4,3], [7,6,5]]))
start_state = Board.Board(np.array([[1,2,3], [4,5,6], [8,7,0]]))
# start_state = Board.Board(np.array([[5,2,8], [4,1,7], [0,3,6]]))
# print(start_state.print_board())
algo = Algorithms.Algorithms(start_state, goal_state)

# moves_list = algo.bfs()
# moves_list = algo.dfs(10)
# moves_list = algo.iddfs(10)
# moves_list = algo.greedy_search()
# print(moves_list)


def checker(premutation):

    premuta = premutation.flatten()
    # print(premuta)
    num_inversion = 0

    for i in range(len(premuta) - 1):
        for j in range(i+1, len(premuta)):
            if premuta[j] and premuta[i] > premuta[j]:
                num_inversion += 1

    # print(num_inversion)
    if num_inversion % 2 == 0:
        return True
    else:
        return False

print(checker(start_state.get_board()))