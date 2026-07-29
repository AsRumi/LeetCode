"""
1668. Maximum Repeating Substring: https://leetcode.com/problems/maximum-repeating-substring/description/
"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        
        def kmpPatternFinder(string, pattern):
            n = len(pattern)
            pi = [0] * n
            k = 0
            for i in range(1, n):
                while k > 0 and pattern[i] != pattern[k]:
                    k = pi[k - 1]
                if pattern[i] == pattern[k]:
                    k += 1
                pi[i] = k
            
            
            
            return False
        
        return count
    
answer = Solution()
maxRepeating = answer.maxRepeating(sequence = "ababc", word = "ab")
print(f"Max Repeating: {maxRepeating}")