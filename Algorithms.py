import numpy as np
import Node
import Board

# create a node that includes 
def create_node(start, parent, action, depth):
        return Node.Node(start, parent, action, depth)

# generate the possible moves
def generate_move(node):
    # return a list of expanded nodes
    possible_moves = []
    possible_moves.append(create_node( node.state.move_up(), node, "U", node.depth + 1))
    possible_moves.append(create_node( node.state.move_down(), node, "D", node.depth + 1))
    possible_moves.append(create_node( node.state.move_right(), node, "R", node.depth + 1))
    possible_moves.append(create_node( node.state.move_left(), node, "L", node.depth + 1))

    # filther the list and remove the moves that are impossible (move function return None)
    possible_moves = [node for node in possible_moves if node.state != None]

    return possible_moves

class Algorithms:

    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        
    # BFS = Breadth-first search
    def bfs(self):
        # A list (can be act as a queue) for the nodes
        nodes = []

        # create the queue with root node in it
        nodes.append(create_node(self.start_state, None, None, 0))

        # print(nodes[0].state.print_board())

        while nodes:
            # end of states 
            if len(nodes) == 0: 
                return None
            
            # take the node from the front of the queue
            node = nodes.pop(0)
            # print(node.state.print_board())
            # Append the move we made to moves
            # if this node is the goal, return the moves it took to get here
            if np.array_equal(node.state.get_board(), self.goal_state):
                move_list = []

                temp = node
                while True:
                    if temp.actions:
                        move_list.insert(0, temp.actions)
                        if temp.depth == 1:
                            break
                        temp = temp.parent
                    else:
                        print("goal state and start state is same from the beginning")
                        break
                return move_list
                # break

            # Expand the node and add all the expanions to front of the queue.
            nodes.extend( generate_move(node))

    # Dfs = depth-first search
    def dfs(self, depth=10):
        # A list (can be act as a stack) for the nodes
        nodes = []

        # create the stack with root node in it
        nodes.append(create_node(self.start_state, None, None, 0))
        
        while nodes:

            if len(nodes) == 0:
                return None
            
            node = nodes.pop(0)
            # print(node.state.print_board())

            if np.array_equal(node.state.get_board(), self.goal_state):
                move_list = []

                temp = node
                while True:
                    if temp.actions:
                        move_list.insert(0, temp.actions)
                        if temp.depth == 1:
                            break
                        temp = temp.parent
                    else:
                        print("goal state and start state is same from the beginning")
                        break
                return move_list

            # stop it from getting "stuck" in left side of the tree
            if node.depth < depth:
                # generate the new moves
                new_moves = generate_move(node)
                # attached the remaming moves after new ones (finish the left branch first)
                new_moves.extend(nodes)
                # assign them back to the nodes list
                nodes = new_moves
                # print("nodes depth: ", node.depth)


    # Iterative deepening depth first search
    def iddfs(self, depth):
        for i in range(depth):
            moves = self.dfs(i)

            if moves != None:
                return moves
            # print(moves)
    
    # Greedy search
    def greedy_search(self):
        
        nodes = []

        nodes.append(create_node(self.start_state, None, None, 0))

        while nodes:

            if len(nodes) == 0:
                return None

            node = nodes.pop(0)
            print(node.state.print_board())

            if np.array_equal(node.state.get_board(), self.goal_state):
                move_list = []

                temp = node
                while True:
                    if temp.actions:
                        move_list.insert(0, temp.actions)
                        if temp.depth == 1:
                            break
                        temp = temp.parent
                    else:
                        print("goal state and start state is same from the beginning")
                        break
                return move_list

            # assign a score for each move 
            # pick the most closest score 
            # repeat till the goal state is reached
            
            # print("Here we calculate the score")

            new_moves = generate_move(node)

            scores = []
            for move in new_moves:
                scores.append(self.heuristic(move))
            
            
            min_dist_index = np.argmin(scores)
            # print(min_dist_index)

            nodes = [new_moves[min_dist_index]]
            # print(nodes.state.get_board())

    # manhattan distance
    def heuristic(self, move):

        state = move.state.get_board()
        goal = self.goal_state

        score = 0
        for i in range(9):
            x1, y1 = np.where(state == i)
            # print("state: ", x1[0], y1[0])
            x2, y2 = np.where(goal == i)
            
            # print("goal: ", x2[0], y2[0])
            score += abs(x1[0] - x2[0]) + abs(y1[0] - y2[0])

        
        return score
    
