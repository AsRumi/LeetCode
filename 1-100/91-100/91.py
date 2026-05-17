"""
Docstring for 91-100.91
191. Number of 1 Bits https://leetcode.com/problems/number-of-1-bits/description/
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        return binary.count('1')
    
answer = Solution()
hammingWeight = answer.hammingWeight(n = 2147483645)
print(f"Hamming Weight: {hammingWeight}")