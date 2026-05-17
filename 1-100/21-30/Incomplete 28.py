# 2352. Equal Row and Column Pairs
from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        i = 0
        rotated_grid = []
        element_set = set()
        while i<len(grid):
            j = 0
            row = []
            while j<len(grid[i]):
                row.append(grid[j][i])
                element_set.add(grid[j][i])
                j += 1
            rotated_grid.append(row)
            i += 1
        if len(element_set) == 1:
            return len(grid) * 2
        counter1 = Counter(tuple(row) for row in grid)
        counter2 = Counter(tuple(row) for row in rotated_grid)
        equalPairs = 0
        seen = []
        for row in grid:
            if (row in rotated_grid) and (row not in seen):
                equalPairs += max(counter1.get(tuple(row)), counter2.get(tuple(row)))
            seen.append(row)
        return equalPairs
    
answer = Solution()
grid = [[3,3,3,6,18,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[1,1,1,11,19,1,1,1,1,1],[3,3,3,18,19,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,1,6,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3]]
equalPairs = answer.equalPairs(grid = grid)
print(f"Equal Pairs: {equalPairs}")