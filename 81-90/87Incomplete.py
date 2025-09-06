"""
131. Palindrome Partitioning
"""
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []
        def checkPalindrome(s: str):
            if s == s[::-1]:
                return True
            return False
        def backtrack(i):
            
            return
        return res
    
ans = Solution()
partition = ans.partition(s = "aab")
print(f"Partition: {partition}")

# s = "racecar"
# print(s[:1])