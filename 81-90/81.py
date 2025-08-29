"""
78. Subsets https://leetcode.com/problems/subsets/description/
"""
from typing import List
class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        def backtrack(i):
            if i == n:
                res.append(sol[:]) # Not just sol because you want the snapshot of sol at current time, not a reference to sol.
                return
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res

answer = Solution()
subsets = answer.subsets(nums = [1, 2, 3])
print(f"Subsets: {subsets}")