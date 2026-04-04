"""
5. Longest Palindromic Substring https://leetcode.com/problems/longest-palindromic-substring/description/
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp_table = [[0] * n for _ in range(n)]
        
        max_length, index = 1, 0
        
        for i in range(n):
            dp_table[i][i] = 1
    
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                        
                if s[i] == s[j]:
                    if i == j - 1:
                        dp_table[i][j] = 2
                    elif dp_table[i+1][j-1] != 0:
                        dp_table[i][j] = dp_table[i+1][j-1] + 2
                    else:
                        dp_table[i][j] = 0
                    
                else:
                    dp_table[i][j] = 0
                    
                if dp_table[i][j] > max_length:
                    max_length = dp_table[i][j]
                    index = i
        return s[int(index): int(index + max_length)]
    
answer = Solution()
longestPalindrome = answer.longestPalindrome(s = "akabaasdqwdsa")
print(f"Longest Palindrome: {longestPalindrome}")