class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        row_flips = 0
        col_flips = 0
        for row in grid:
            first = 0
            last = len(row) - 1
            while(first<=last):
                if row[first] != row[last]:
                    row_flips += 1
                first += 1
                last -= 1
        transposeGrid = [list(row) for row in zip(*grid)]
        for row in transposeGrid:
            first = 0
            last = len(row) - 1
            while(first<=last):
                if row[first] != row[last]:
                    col_flips += 1
                first += 1
                last -= 1
        return min(row_flips, col_flips)
    
answer = Solution()
minFlips = answer.minFlips(grid = [[1,0,0],[0,0,0],[0,0,1]])
print(f"Minimum Flips: {minFlips}")