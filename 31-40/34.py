# 2914. Minimum Number of Changes To Make Binary String Beautiful

class Solution:
    def minChanges(self, s: str) -> int:
        if len(s) == 2:
            return 0 if s[0] == s[1] else 1
        i = 1
        min_changes = 0
        while i < len(s):
            prev = s[i-1]
            current = s[i]
            if current == prev:
                i += 1
                continue
            if (i) % 2 == 0:
                i += 1
                continue
            min_changes += 1
            i += 2
        return min_changes
    
answer = Solution()
min_changes = answer.minChanges(s = "1001")
print(f"Minimum Changes: {min_changes}")