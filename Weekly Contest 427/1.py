class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        """
        Function takes a list as an input (array) and returns another list as an ouput (array).
        Read the problem statement and let me know more about what is needed.
        """
        # Write code to transform array here:
        result = []
        copy = nums * 3
        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(nums[i])
            elif nums[i] > 0:
                position = nums[i]//len(nums)
                position = nums[i] - (position*len(nums))
                position = len(nums) + i + position
                result.append(copy[position])
            else:
                x = abs(nums[i])
                position = x//len(nums)
                position = x - (position*len(nums))
                position = len(nums) + i - position
                result.append(copy[position])
        return result

answer = Solution()
transformed_array = answer.constructTransformedArray(nums = [3, -2, 7, 10])
print(f"Transformed Array: {transformed_array}")
