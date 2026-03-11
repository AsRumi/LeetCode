class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        prev_increase, cur_increase = 0,1
        res = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_increase += 1
            else:
                prev_increase, cur_increase = cur_increase, 1
            res = max(res, cur_increase // 2, min(prev_increase, cur_increase))
        return res
    
answer = Solution()
max_increasing_subarray = answer.maxIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1])
print(f"Max Increasing Subarrays: {max_increasing_subarray}")