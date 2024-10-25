class Solution:
    def doesAliceWin(self, s: str) -> bool:
        total = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
        if total == 0:
            return False
        return True

answer = Solution()
doesAliceWin = answer.doesAliceWin(s = 'leetcoder')
print(f"Alice Wins: {doesAliceWin}")