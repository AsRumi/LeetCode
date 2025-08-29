"""
You can use this script to create any number of graphs for your DFS/BFS or navigation algorithms.

MVP:
Goal: Create a 2D array of 0s and 1s where 1s represent walls and 0s represent walkable routes based on user input.
The source of the graph starts from (0,0) and ends at (N-1,N-1) where N is the total number of rows and columns.
The graph must have at least 1 valid path from source to destination.

Additional Features:
Feature: Able to create shortest route, with minimum number of movements.
Feature: Able to create circular paths (Number of circular paths can be taken as an input but maximum will be based on a formula that calculates the maximum number of circular paths that the graph can accomodate).
Feature: Able to create exact number of solutions (Except the graph where every path is 0).
"""
import numpy as np
import random
class Map:

    def __init__(self, dimension):
        # Create an array with dimension x dimension shape.
        self.map = np.ones(shape = (dimension, dimension), dtype = int)
        self.dimension = dimension

    def showGraph(self):
        for row in self.map:
            for path in row:
                print(path, end="\t")
            print("\n")
        return None

    def createShortest(self):
        """
        The shortest path from source to destination is N times right and N times down, but can be so in any order.
        """
        rightMoves = self.dimension - 1
        downMoves = self.dimension - 1
        i, j = 0, 0
        self.map[i][j] = 0
        while rightMoves > 0 or downMoves > 0:
            available_moves = []
            if rightMoves > 0:
                available_moves.append('right')
            if downMoves > 0:
                available_moves.append('down')
            move = random.choice(available_moves)
            if move == 'right':
                j += 1
                rightMoves -= 1
            else:
                i += 1
                downMoves -= 1
            self.map[i][j] = 0
        return None

    def createRoute(self):
        """
        You can only have a set number of routes from 0,0 to N,N.
        If N = 2, You need 2 rights and 2 downs to get to the last node.
        The combination can be anything of the above directions.
        But this is only the shortest route.
        """

        return None

    def createCircular(self, paths):

        return None
    
    def createPaths(self, paths):
        from itertools import combinations
        
        # Reset the map
        self.map = np.ones(shape=(self.dimension, self.dimension), dtype=int)
        
        # Calculate total moves needed
        total_moves = 2 * (self.dimension - 1)
        moves_per_direction = self.dimension - 1
        
        # Generate all possible shortest paths
        # We choose positions for 'right' moves, rest will be 'down'
        all_possible_paths = list(combinations(range(total_moves), moves_per_direction))
        
        # Check if requested paths exceed possible paths
        if paths > len(all_possible_paths):
            print(f"Maximum possible distinct paths: {len(all_possible_paths)}")
            paths = len(all_possible_paths)
        
        # Randomly select the requested number of paths
        selected_combinations = random.sample(all_possible_paths, paths)
        
        # Convert each combination to actual path and mark on map
        for combo in selected_combinations:
            i, j = 0, 0
            self.map[i][j] = 0
            
            for move_index in range(total_moves):
                if move_index in combo:
                    j += 1  # Right move
                else:
                    i += 1  # Down move
                
                if i < self.dimension and j < self.dimension:
                    self.map[i][j] = 0
        
        return None
    
myMap = Map(dimension = 7)
myMap.createPaths(2)
myMap.showGraph()