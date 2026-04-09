"""
647. Palindromic Substrings https://leetcode.com/problems/palindromic-substrings/description/
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        total_palindromes = len(s)
        for i, _ in enumerate(s):
            j = 1
            while (i - j >= 0) and (i + j < len(s)) and (s[i - j] == s[i + j]):
                total_palindromes += 1
                j += 1
        for i, _ in enumerate(s):
            left, right = i, i + 1
            if right < len(s) and s[left] == s[right]:
                total_palindromes += 1
                j = 1
                while (left - j >= 0) and (right + j < len(s)) and (s[left - j] == s[right + j]):
                    total_palindromes += 1
                    j += 1
        return total_palindromes
    
answer = Solution()
countSubstrings = answer.countSubstrings(s = "aaa")
print(f"Count Substrings: {countSubstrings}")