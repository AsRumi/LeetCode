"""
994. Rotting Oranges https://leetcode.com/problems/rotting-oranges/description/

Very similar solution to Water and Gates.
"""

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        max_x = len(grid)
        max_y = len(grid[0])
        queue = deque()
        max_minute = 0
        fresh_count = 0
        
        for x, row in enumerate(grid):
            for y, item in enumerate(row):
                if item == 2:
                    queue.append((x, y, 0))
                if item == 1:
                    fresh_count += 1
                    
        while len(queue) > 0: 
            x, y, minute = queue.popleft()
            max_minute = max(max_minute, minute)
            
            directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            
            for direction in directions:
                new_x, new_y = direction
                if new_x < 0 or new_x >= max_x or new_y < 0 or new_y >= max_y:
                    pass
                else:
                    if grid[new_x][new_y] == 1:
                        fresh_count -= 1
                        grid[new_x][new_y] = 2
                        queue.append((new_x, new_y, minute + 1))
        
        if fresh_count == 0:
            return max_minute
        return -1
    
answer = Solution()
orangesRotting = answer.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]])
print(f"Oranges Rotting: {orangesRotting}")