# 36. Valid Sudoku
from collections import Counter
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def checkLine(line):
            number_counts = Counter(line)
            del number_counts['.']
            number_counts = number_counts.most_common()
            if len(number_counts) == 0:
                return True
            if number_counts[0][1] > 1:
                return False
            return True
        
        for row in board:
            if not checkLine(line = row):
                return False
        
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            if not checkLine(line = col):
                return False
        
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                subgrid = []
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        subgrid.append(board[row][col])
                if not checkLine(subgrid):
                    return False
        return True
    
answer = Solution()
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".",".",".",".",".","."]]
valid = answer.isValidSudoku(board)
print(f"Valid Sudoku: {valid}")