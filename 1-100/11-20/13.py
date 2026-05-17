'''
Idea: Have two pointers, left and right.
Check for these conditions:
Lenght of the array must be greater than 1 to find pairs.
Left must be less than right, it can be equal since at that position we need to reset the pointers.
How to reset the pointers: increment left by one and reset right to last position on nums.
If a matching pair is found, pop both from the list and reset left to 0 and right to last position on the list.

Solved but time complexity is too large.
'''
from collections import Counter
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        left = 0
        right = len(nums)-1
        count = 0
        while(len(nums)>1 and left<=right):
            if(left==right):
                right = len(nums)-1
                left+=1
                continue
            if(nums[left]+nums[right]==k):
                del nums[left]
                del nums[right-1]
                right = len(nums) - 1
                left = 0
                count += 1
            else:
                right -= 1
        return count

answer = Solution()
numbers = [82,85,16,61,14,3,81,59,31,68,23,65,70,90,67,49,41,31,59,74,62,32,12,16,23,38,46,70,66,9,85,75,9,43,10,71,30,9,26,9,49,83,82,55,38,59,88,12,15,71,6,62,53,88,88,33,28,34,44,80,86,24,67,20,80,81,71,6,66,48,53,7,22,9,1,56,78,14,45,80,62,3,72,73,13,71,23,26,71,63,39,29,88,36,27,70,21,6,43,7,82,62,21,24,37,89,53,3,66,21,47,7,38,12,21,31,16,44,45,87,37,5,11,25,77,16,78,81,80,86,12,70,29,63,79,73,50,74,27,50,64,3,53,78,69,77,55,77,59,4,70,32,56,54,89,56,53,60,33,25,41,30,9,51,3,22,19,51,58,17,9,60,81,12,16,82,65,54,17,89,15,66,15,17,57,39,22,80,10,86,85,65,14,64,87,64,54,13,5,18,30,26,34,3,30,42,4,51,41,78,49,38,17,85,17,59,51,46,86,59,53,4,82,77,49,22,6,20,36,70,13,24,61,48,79,14,19,35,84,76,87,46,30,6,45,86,71,73,61,38,62,27,90,85,36,62,58,14,6,52,45,82,46,85,89,69,87,62,86,52,51,25,62,55,86,18,32,37,26,56,69,87,29,68,13,17,22,47,16,33,65,24,82,1,34,53,57,27,67,40,25]
pairs = answer.maxOperations(numbers, 80)
print(f"Maximum number of K-Sum pairs: {pairs}")