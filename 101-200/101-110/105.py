"""
213. House Robber II https://leetcode.com/problems/house-robber-ii/description/
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)
        
        def profit_calculator(houses: List[int]) -> int:
            profit, i = [], 0
            
            while i < len(houses):
                if i == 0:
                    profit.append(houses[i])
                elif i == 1:
                    profit.append(max(houses[0], houses[1]))
                else:
                    profit.append(max(houses[i] + profit[i-2], profit[i-1]))
                i += 1
            
            return max(profit[i-2], profit[i-1])    
        
        return max(profit_calculator(houses = nums[:-1]), 
                   profit_calculator(houses = nums[1: ]))
    
answer = Solution()
rob = answer.rob([2, 3, 2])
print(f"Rob: {rob}")