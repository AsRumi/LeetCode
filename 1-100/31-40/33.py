# 796. Rotate String

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        rotated_string = s
        for i in range(len(s)):
            rotated_string += s[i]
            rotated_string = rotated_string[1:]
            if rotated_string == goal:
                return True
        return False
    
answer = Solution()
rotate_string = answer.rotateString(s = "abcde", goal = "cdeab")
print(f"Rotate String: {rotate_string}")