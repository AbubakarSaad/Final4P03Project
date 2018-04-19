import numpy as np


class Node: 

    def __init__(self, state, parent, actions, depth):
        # state of the of the puzzle instance
        self.state = state

        # parent node of the puzzle instance
        self.parent = parent

        # actions that generated this puzzle instance
        self.actions = actions

        # depth of the current puzzle instance
        self.depth = depth
        
