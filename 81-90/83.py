"""
40. Combination Sum II https://leetcode.com/problems/combination-sum-ii/description/
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        l = len(candidates)
        candidates.sort()
        def backtrack(start):
            if sum(sol) > target or start >= l:
                return
            elif sum(sol) == target:
                res.append(sol[:])
                return
            i = start
            while(i<l):
                if i > start and candidates[i] == candidates[i-1]:
                    i += 1
                    continue
                sol.append(candidates[i])
                backtrack(i + 1)
                sol.pop()
                i += 1
        backtrack(0)
        return res
    
ans = Solution()
combos = ans.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
print(f"Combination Sums: {combos}")