# 84. Largest Rectangle in Histogram

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        currentLargest = largest = heights[0]
        width = 1
        area = largest * width
        for i in range(1, len(heights)):
            currentLargest = 0
        return largest
    
answer = Solution()
largest_rect = answer.largestRectangleArea(heights = [2,1,5,6,2,3])
print(f"Largest Rectangle Area: {largest_rect}")