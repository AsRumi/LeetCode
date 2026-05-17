"""
39. Combination Sum https://leetcode.com/problems/combination-sum/description/
"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = len(candidates)
        res, sol = [], []
        def backtrack(i):
            if sum(sol) > target or i >= l:
                return
            elif sum(sol) == target:
                res.append(sol[:])
                return
            while(i<l):
                sol.append(candidates[i])
                backtrack(i)
                sol.pop()
                i += 1

        backtrack(0)
        return res
    
ans = Solution()
combos = ans.combinationSum(candidates = [2,3,6,7], target = 7)
print(f"Combinations: {combos}")