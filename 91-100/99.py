"""
695. Max Area of Island https://leetcode.com/problems/max-area-of-island/description/
"""

from typing import List

class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_row = len(grid)
        max_col = len(grid[0])
        max_area = 0
                
        def marked_dfs(x, y):
            if (x < 0) or (x >= max_row) or (y < 0) or (y >= max_col):
                return 0
            
            if grid[x][y] == 0:
                return 0
            
            directions = {
                "right": (x+1, y),
                "left": (x-1, y),
                "up": (x, y+1),
                "down": (x, y-1)
            }
            
            grid[x][y] = 0
        
            return 1 + marked_dfs(*directions["right"]) + marked_dfs(*directions["left"]) + marked_dfs(*directions["up"]) + marked_dfs(*directions["down"])
        
        for x, row in enumerate(grid):
            for y, unit in enumerate(row):
                if unit == 1:
                    area = marked_dfs(x, y)
                    max_area = area if max_area < area else max_area
        
        return max_area
    
answer = Solution()
maxAreaOfIsland = answer.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(f"Max Area of Island: {maxAreaOfIsland}")