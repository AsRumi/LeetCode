"""
79. Word Search: https://leetcode.com/problems/word-search/description/
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        word = list(word)

        def searchLetter(m, n, letter) -> bool:
            if m < 0 or n < 0 or m > (rows-1) or n > (cols-1):
                return False
            if board[m][n] == letter:
                return True
            return False

        def backtrack(m, n):
            
            if len(word) == 0:
                return True
            
            if searchLetter(m-1, n, word[0]) and board[m-1][n] != '*' :
                tempSearchLetter = word.pop(0)
                tempBoardLetter = board[m-1][n]
                board[m-1][n] = '*'
                if backtrack(m-1, n):
                    return True
                board[m-1][n] = tempBoardLetter
                word.insert(0, tempSearchLetter)
            
            if searchLetter(m+1, n, word[0]) and board[m+1][n] != '*':
                tempSearchLetter = word.pop(0)
                tempBoardLetter = board[m+1][n]
                board[m+1][n] = '*'
                if backtrack(m+1, n):
                    return True
                board[m+1][n] = tempBoardLetter
                word.insert(0, tempSearchLetter)

            if searchLetter(m, n-1, word[0]) and board[m][n-1] != '*':
                tempSearchLetter = word.pop(0)
                tempBoardLetter = board[m][n-1]
                board[m][n-1] = '*'
                if backtrack(m, n-1):
                    return True
                board[m][n-1] = tempBoardLetter
                word.insert(0, tempSearchLetter)
            
            if searchLetter(m, n+1, word[0]) and board[m][n+1] != '*':
                tempSearchLetter = word.pop(0)
                tempBoardLetter = board[m][n+1]
                board[m][n+1] = '*'
                if backtrack(m, n+1):
                    return True
                board[m][n+1] = tempBoardLetter
                word.insert(0, tempSearchLetter)
            
            return False

        i, j = 0, 0
        while i < rows:
            while j < cols:
                if board[i][j] == word[0]:
                    temp = word.pop(0)
                    board[i][j] = '*'
                    if backtrack(i, j):
                        return True
                    word.insert(0, temp)
                    board[i][j] = temp
                j += 1
            j = 0
            i += 1

        return False
    
ans = Solution()
exist = ans.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
print(f"Exist: {exist}")