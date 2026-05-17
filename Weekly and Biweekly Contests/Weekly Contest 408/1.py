class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        sum_single = sum([i for i in nums if i < 10])
        sum_double = sum([i for i in nums if i >= 10])
        if sum_single == sum_double:
            return False
        return True
    
answer = Solution()
canAliceWin = answer.canAliceWin(nums = [1,2,3,4,10])
print(f"Can Alice Win: {canAliceWin}")