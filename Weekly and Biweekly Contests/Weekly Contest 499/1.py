class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        validElements = []
        for i, num in enumerate(nums):
            if i == 0 or i == len(nums) - 1:
                validElements.append(num)
                continue
            if num > max(nums[:i]) or num > max(nums[i + 1:]):
                validElements.append(num)
        return validElements
    
answer = Solution()
findValidElements = answer.findValidElements(nums = [1,2,4,2,3,2])
print(f"Valid Elements: {findValidElements}")