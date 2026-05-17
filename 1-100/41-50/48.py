# 15. 3Sum
# Works partially. Idea was to check if the difference of two numbers was present in the list or not, so that the sum would amount to 0.
# Problem: No regard for index positions, which is a condition of the problem.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 3:
            return [] if sum(nums) != 0 else nums
        nums.sort()
        if nums[-1] <= 0:
            if nums.count(0) >= 3:
                return [0, 0, 0]
            return []
        if nums[0] >= 0:
            if nums.count(0) >= 3:
                return [0, 0, 0]
            return []
        triplets = []
        seen = set()
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] in seen and nums[right] in seen:
                left += 1
                right -= 1
                continue
            difference = nums[right] + nums[left]
            difference *= -1
            if difference in nums:
                triplets.append([nums[left], nums[right], difference])
                seen.add(nums[left])
                seen.add(nums[right])
                seen.add(difference)
            left += 1
            right -= 1
        return triplets
    
answer = Solution()
three_sum = answer.threeSum(nums = [-5, -4, -4, -3, -2, 0, 3, 6, 7, 9])
print(f"Three Sum: {three_sum}")