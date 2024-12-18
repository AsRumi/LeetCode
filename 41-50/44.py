# Valid Anagram

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
        if s == t:
            return True
        return False
    
answer = Solution()
is_anagram = answer.isAnagram(s = "aa", t = "a")
print(f"Is Anagram: {is_anagram}")