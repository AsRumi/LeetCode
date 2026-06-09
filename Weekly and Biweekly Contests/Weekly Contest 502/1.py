class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        if len(s) < 2:
            return True
        if len(s) == 2:
            if abs(int(s[0]) - int(s[1])) > 2:
                return False
            else:
                return True
        for i in range(1, len(s) - 1):
            if (abs(int(s[i-1]) - int(s[i])) > 2) or (abs(int(s[i+1]) - int(s[i])) > 2):
                return False
        return True
    
answer = Solution()
isAdjacentDiff = answer.isAdjacentDiffAtMostTwo("132")
print(f"Is Adjacent Difference At Most Two: {isAdjacentDiff}")