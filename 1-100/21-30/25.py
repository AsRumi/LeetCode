# 2390. Removing stars from a String
from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        stack2 = deque()
        for item in s:
            if item == "*":
                stack2.pop()
            else:
                stack2.append(item)
        ans = ""
        i = 0
        total = len(stack2)
        while i<total:
            ans += stack2.popleft()
            i += 1
        return ans
    
answer = Solution()
removeStars = answer.removeStars(s = "leet**cod*e")
print(f"After removing stars: {removeStars}")