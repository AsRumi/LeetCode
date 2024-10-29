#2501. Longest Square Streak in an Array
import math
class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums.sort(reverse = True)
        squares = []
        for num in nums:
            square_root = math.sqrt(num)
            if square_root % 1 == 0 and (square_root in nums):
                squares.append(num)
                squares.append(square_root)
        squares = list(set(squares))
        squares.sort()
        my_dict = {}
        for i in range(2, 100001):
            j = i
            if j**2 <= 100000:
                my_dict[i] = []
                my_dict[i].append(j)
                while(j**2<100000):
                    my_dict[i].append(j**2)
                    j = j**2
        print(len(my_dict.keys()))
        return 0

answer = Solution()
longestSquareStreak = answer.longestSquareStreak(nums = [4,3,6,16,8,81,6561])
print(f"Longest Square Streak: {longestSquareStreak}")