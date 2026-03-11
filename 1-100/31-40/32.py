# 962. Maximum Width Ramp

class Solution:
    def maxWidthRampExceedsMemoryLimit(self, nums: list[int]) -> int:
        indexed_nums = [(value, index) for index, value in enumerate(nums)]
        sorted_nums = sorted(indexed_nums, key = lambda x:x[0])
        lengths = []
        for i in range(len(sorted_nums)):
            for j in range(i + 1, len(sorted_nums)):
                if sorted_nums[i][1] < sorted_nums[j][1]:
                    lengths.append(sorted_nums[j][1] - sorted_nums[i][1])
        return max(lengths) if lengths else 0
    
    def maxWidthRamp(self, nums: list[int]) -> int:
        indexed_nums = [(value, index) for index, value in enumerate(nums)]
        sorted_nums = sorted(indexed_nums, key=lambda x: x[0])
        max_width = 0
        min_index = sorted_nums[0][1]
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i][1] < min_index:
                min_index = sorted_nums[i][1]
            else:
                max_width = max(max_width, sorted_nums[i][1] - min_index)
        return max_width
    
answer = Solution()
max_width_ramp = answer.maxWidthRamp(nums = [1,0])
print(f"Max Width Ramp: {max_width_ramp}")