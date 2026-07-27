"""
118. Pascal's Triangle https://leetcode.com/problems/pascals-triangle
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        result = [[1]]
        prevRow = [1]
        for i in range(2, numRows + 1):
            currentRow = []
            for j in range(0, i):
                if j == 0:
                    currentRow.append(1)
                elif j == i - 1:
                    currentRow.append(1)
                else:
                    currentRow.append(prevRow[j - 1] + prevRow[j])
            result.append(currentRow)
            prevRow = currentRow
        return result
    
answer = Solution()
generate = answer.generate(5)
print(f"Generate: {generate}")