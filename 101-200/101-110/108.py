"""
134. Gas Station https://leetcode.com/problems/gas-station/description/
"""

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_d = 0
        starting_index = 0
        gas_level = 0
        for i in range(len(gas)):
            difference = gas[i] - cost[i]
            sum_d += difference
            gas_level += difference
            if gas_level < 0:
                gas_level = 0
                starting_index = i + 1
        return starting_index if sum_d >= 0 else -1
    
answer = Solution()
canComplete = answer.canCompleteCircuit(gas = [5,1,2,3,4], cost = [4,4,1,5,1])
print(f"Can complete: {canComplete}")