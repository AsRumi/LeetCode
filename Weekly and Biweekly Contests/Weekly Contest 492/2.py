"""
3862. Find the Smallest Balanced Index https://leetcode.com/problems/find-the-smallest-balanced-index/description/
"""

class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        # Go reverse, calculate sum at the same time.
        rsum = 0
        reversed_nums = []
        n = 0
        for num in nums[::-1]:
            reversed_nums.append(num)
            rsum += num
            n += 1
        product = 1
        i = 0
        answer = []
        # org = (n-1) - index
        while i < n:
            rsum = rsum - reversed_nums[i]
            if product == rsum:
                answer.append((n - 1) - i)
            if product > rsum:
                break
            product *= reversed_nums[i]
            i += 1
        if len(answer) == 0:
            return -1
        return min(answer)
    
answer = Solution()
smallestBI = answer.smallestBalancedIndex(nums = [2, 4, 10, 1, 8, 2])
print(f"Smallest Balanced Index: {smallestBI}")