"""
119. Pascal's Triangle II https://leetcode.com/problems/pascals-triangle-ii/description/
"""

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prevRow = [1]
        for i in range(1, rowIndex + 2):
            currentRow = []
            for j in range(0, i):
                if j == 0:
                    currentRow.append(1)
                elif j == i - 1:
                    currentRow.append(1)
                else:
                    currentRow.append(prevRow[j - 1] + prevRow[j])
            prevRow = currentRow
        return currentRow
    
answer = Solution()
getRow = answer.getRow(3)
print(f"Get Row: {getRow}")