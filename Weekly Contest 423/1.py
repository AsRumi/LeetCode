class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        def strictlyIncreasing(idx):
            for i in range(idx, idx + k - 1):
                if nums[i] >= nums[i+1]:
                    return False
            return True
        for idx in range(len(nums)-k-k+1):
            if strictlyIncreasing(idx) and strictlyIncreasing(idx+k):
                return True
        return False
    
answer = Solution()
has_increasing_subarray = answer.hasIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1], k = 3)
print(f"Has Increasing Subarrays: {has_increasing_subarray}")