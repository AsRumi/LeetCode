"""
46. Permutations https://leetcode.com/problems/permutations/description/
"""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        state = nums.copy()
        def backtrack():
            i = 0
            while i < len(state):
                temp = state[i]
                sol.append(state[i])
                state.pop(i)
                backtrack()
                state.insert(i, temp)
                sol.pop()
                i += 1
            if len(sol) == len(nums):
                res.append(sol[:])
                return
        backtrack()
        return res
    
ans = Solution()
permutations = ans.permute(nums = [1, 2, 3])
print(f"Permutations: {permutations}")