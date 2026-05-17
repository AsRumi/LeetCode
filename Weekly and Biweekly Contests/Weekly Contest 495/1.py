"""
3884. First Matching Character From Both Ends https://leetcode.com/problems/first-matching-character-from-both-ends/description/
"""

class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        index, i, n = -1, 0, len(s)
        while i < n / 2:
            if s[i] == s[n - i - 1]:
                index = i
                break
            i += 1
        return index
    
answer = Solution()
firstMatchingIndex = answer.firstMatchingIndex(s = "abcacbd")
print(f"First Matching Index: {firstMatchingIndex}")