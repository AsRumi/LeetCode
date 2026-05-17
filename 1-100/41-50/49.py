# 11. Container with most water

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
    
answer = Solution()
max_area = answer.maxArea(height = [1,8,6,2,5,4,8,3,7])
print(f"Max Area: {max_area}")