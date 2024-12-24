# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Kadane's Algorithm
        currentSum, globalSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            currentSum = max(currentSum + nums[i], nums[i])
            globalSum = globalSum if globalSum > currentSum else currentSum
        return globalSum
    
answer = Solution()
max_sub_array = answer.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])
print(f"Max Sub Array: {max_sub_array}")