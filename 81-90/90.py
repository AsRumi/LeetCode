"""
Docstring for 81-90.90
136. Single Number https://leetcode.com/problems/single-number/description/?envType=problem-list-v2&envId=bit-manipulation
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single = single ^ num
        return single
    
answer = Solution()
singleNumber = answer.singleNumber(nums = [4, 1, 2, 1, 2])
print(f"Single Number: {singleNumber}")