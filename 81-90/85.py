"""
90. Subsets II https://leetcode.com/problems/subsets-ii/description/
"""
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()
        l = len(nums)
        def backtrack(start):
            if start == l:
                res.append(sol[:])
                return
            else:
                res.append(sol[:])
            i = start
            while(i < l):
                if i > start and nums[i] == nums[i-1]:
                    i += 1
                    continue
                sol.append(nums[i])
                backtrack(i+1)
                sol.pop()
                i += 1
        backtrack(0)
        return res
    
    def subsetsWithDupBF(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        l = len(nums)
        nums.sort(reverse=True)
        def backtrack(i):
            if i == l:
                if sol not in res:
                    res.append(sol[:])
                    return
                else:
                    return
            backtrack(i+1)
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res
    
ans = Solution()
subsets = ans.subsetsWithDup(nums = [1, 1, 2, 3, 3])
print(f"Subsets without duplication: {subsets}")