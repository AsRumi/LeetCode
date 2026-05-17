"""
55. Jump Game https://leetcode.com/problems/jump-game/description/
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal, current = len(nums) - 1, len(nums) - 2
        while current >= 0:
            if nums[current] >= goal - current:
                goal = current
            current -= 1
        return goal == 0

answer = Solution()
canJump = answer.canJump(nums = [2, 3, 1, 1, 4])
print(f"Can Jump: {canJump}")
