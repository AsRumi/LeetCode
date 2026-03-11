"""
74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binarySearch(nums, target):
            start = 0
            end = len(nums)-1
            middle = len(nums) // 2
            while(start <= end):
                middle = start + (end-start) // 2
                if nums[middle] == target:
                    return True
                elif nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
            return False

        for nums in matrix:
            if (target <= nums[-1]) and (target >= nums[0]):
                return binarySearch(nums, target)
        return False
    
answer = Solution()
searchMatrix = answer.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
print(f"Search Matrix: {searchMatrix}")