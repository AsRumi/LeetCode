"""
286. Water and Gates
"""

from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()
        max_x = len(grid)
        max_y = len(grid[0])
        for x, row in enumerate(grid):
            for y, item in enumerate(row):
                if item == 0:
                    queue.append((x, y, 0))
        
        while len(queue) > 0:
            
            x, y, distance = queue.popleft()
            
            directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            
            for direction in directions:
                new_x, new_y = direction
                if new_x < 0 or new_x >= max_x or new_y < 0 or new_y >= max_y:
                    pass
                else: 
                    if grid[new_x][new_y] == 2147483647:
                        grid[new_x][new_y] = distance + 1
                        queue.append((new_x, new_y, distance + 1))
                        
        return None # Grid is modified in place.
    
answer = Solution()
islandsAndTreasures = answer.islandsAndTreasure(grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
])
print(f"Islands and Treasures: {islandsAndTreasures}")