'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10^-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
'''

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sum(nums[0:k])
        prev_sum = max_sum
        i = 1
        while i<=len(nums)-k:
            subArraySum = prev_sum - nums[i-1] + nums[i+k-1]
            prev_sum = subArraySum
            max_sum = subArraySum if subArraySum>max_sum else max_sum
            i+=1
        return max_sum/k
    
answer = Solution()
my_float = answer.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
print(f"Highest Total Average: {my_float}")