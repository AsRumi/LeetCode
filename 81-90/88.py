"""
200. Number of Islands https://leetcode.com/problems/number-of-islands/
"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        def backtrack(m, n):
            grid[m][n] = 'X'
            top = grid[m - 1][n] if m - 1 >= 0 else 0
            if top == '1':
                backtrack(m - 1, n)
            bottom = grid[m + 1][n] if m + 1 < rows else 0
            if bottom == '1':
                backtrack(m + 1, n)
            left = grid[m][n - 1] if n - 1 >= 0 else 0
            if left == '1':
                backtrack(m, n - 1)
            right = grid[m][n + 1] if n + 1 < cols else 0
            if right == '1':
                backtrack(m, n + 1)
            return
        for i, row in enumerate(grid):
            for j, position in enumerate(row):
                if position == '1':
                    islands += 1
                    backtrack(i, j)
        return islands
    
answer = Solution()
numIslands = answer.numIslands(grid = [["1","1","1"],["0","1","0"],["1","1","1"]])

print(f"Num Islands: {numIslands}")