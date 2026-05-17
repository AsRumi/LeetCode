# 167. Two Sum II - Input Array Is Sorted
import math
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)-1
        while True:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
    
answer = Solution()
two_sum = answer.twoSum(numbers = [3,24,50,79,88,150,345], target = 200)
print(f"Two Sum: {two_sum}")