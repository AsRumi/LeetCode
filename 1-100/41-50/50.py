# 42. Trapping Rain Water

class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        while left < right:
            if height[left] >= height[right]:
                right -= 1
                rightMax = max(height[right], rightMax)
                current = height[right]
                currentMax = rightMax
            elif height[left] < height[right]:
                left += 1
                leftMax = max(height[left], leftMax)
                current = height[left]
                currentMax = leftMax
            water += currentMax - current
        return water
    
answer = Solution()
trap = answer.trap(height = [2, 1, 0, 1, 3, 2])
#                            0,1,2,3,4,5,6,7,8,9,10,11
print(f"Trap: {trap}")