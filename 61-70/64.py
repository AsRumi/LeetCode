"""
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        while (low < high):
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
    
answer = Solution()
findMin = answer.findMin(nums = [3,4,5,1,2])
print(f"Find Min: {findMin}")