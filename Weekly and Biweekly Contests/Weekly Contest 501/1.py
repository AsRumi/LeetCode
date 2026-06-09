class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]
    
answer = Solution()
concatWithReverse = answer.concatWithReverse([1,2,3])
print(f"Concat With Reverse: {concatWithReverse}")