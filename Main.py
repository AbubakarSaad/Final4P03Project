import numpy as np
import random, time
import pygame, sys, os
import Board
import Algorithms
import SlidePuzzle


# Checks if the given permutation is solvable
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


# add a generator then shuffle it
def generator():
    # change this to give number n
    while True:
        arr = np.array([[1,2,3], [4,5,6], [7,8,0]])
        random.shuffle([random.shuffle(c) for c in arr])
        
        if checker(arr) == True:
            # print(arr, checker(arr))
            return arr


# start_state = Board.Board(np.array([[1,8,2], [0,4,3], [7,6,5]]))
# start_state = Board.Board(np.array([[1,2,3], [4,0,5], [8,6,7]]))
# ['U', 'D', 'U', 'D', 'U', 'D', 'R', 'D', 'L', 'L', 'U', 'R', 'R', 'D', 'L', 'U', 'L', 'D', 'R', 'R']
# start_state = Board.Board(np.array([[5,2,8], [4,1,7], [0,3,6]]))


def main():
    start_state = np.array([[1,2,3], [4,0,5], [8,6,7]])
    goal_state = np.array([[1,2,3], [4,5,6], [7,8,0]])

    # select the option of permutation
    permutation_input = input("Enter number from 1 to 3. 1) Enter your own permutation 2) Select a simple permutation 3) Generator will generate a random one. Note 3 option could take possibly take longer to solve \n")

    if permutation_input == "1":
        user_per = input("Enter your own permutation, for e.g: [[1,2 3], [4, 5, 6], [0, 7, 8]] \n")
        while checker(np.array(user_per)) != True:
            user_per = input("That permutation was not solvable, Please try again\n")
            start_state = Board.Board(np.array(user_per))
    elif permutation_input == "2":
        print("simple permutation, such as, [[1,2,3][4,5,6],[0,7,8]] has been selected")
        start_state = Board.Board(np.array([[1,2,3], [4,5,6], [7,0,8]]))
    elif permutation_input == "3":
        print("Random generated permutation has been selected")
        start_state = Board.Board(generator())

    print(start_state.get_board())
    select_algo = input("Select the algorithm to execute: 1) BFS 2) DFS 3) IDDFS 4) Greedy Search\n")

    algo = Algorithms.Algorithms(start_state, goal_state)

    start_time = time.time()
    moves_list = []
    if select_algo == "1":
        moves_list = algo.bfs()
    elif select_algo == "2":
        moves_list = algo.dfs()
    elif select_algo == "3":
        depth_level = input("Chose the depth level to travel\n")
        moves_list = algo.iddfs(int(depth_level))
    elif select_algo == "4":
        moves_list = algo.greedy_search()
    end_time = time.time()
    print("Time of execution: ", (end_time - start_time))

    
    
    if moves_list is not None:
        SlidePuzzle.main(start_state.get_board(), moves_list)
    else:
        print("The puzzle has not been completed. Try with a different algorithm")
    


if __name__ == "__main__":
    main()