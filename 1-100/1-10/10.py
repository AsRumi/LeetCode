'''
Shift all the zeros to the end of the array: 0 1 0 3 12 -> 1 3 12 0 0

Solved: 10 Minutes
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        positions = []
        for i in range(0, len(nums)):
            if(nums[i] == 0):
                positions.append(i)
                nums.append(0)
        for i in positions:
            del nums[i]
            for p,i in enumerate(positions):
                positions[p] = i - 1
    
answer = Solution()
answer.moveZeroes([0, 1, 0, 3, 12])