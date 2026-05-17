"""
3861. Minimum Capacity Box https://leetcode.com/problems/minimum-capacity-box/description/
"""

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        index = -1
        min_capacity = float('inf')
        for i in range(len(capacity)):
            if itemSize <= capacity[i]:
                if capacity[i] < min_capacity:
                    min_capacity = capacity[i]
                    index = i
        return index
    
answer = Solution()
minimumIndex = answer.minimumIndex(capacity = [1,5,3,7], itemSize = 3)
print(f"Minimum Index: {minimumIndex}")