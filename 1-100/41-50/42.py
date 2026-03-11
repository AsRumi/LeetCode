# 128. Longest Consecutive Sequence
# Edge cases have not been handled properly
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        maximum, current = 0, 0
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1] == 1):
                current += 1
            else:
                current += 1
                maximum = max(maximum, current)
                current = 0
        if (current > 0) and (nums[-1] - nums[-2] == 1):
            current += 1
        maximum = max(maximum, current)
        return maximum
    
answer = Solution()
longest_sequence = answer.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
print(f"Longest Consecutive Sequence: {longest_sequence}")