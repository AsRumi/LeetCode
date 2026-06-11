class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        scores = []
        for i, num in enumerate(nums):
            j = i + 1
            currentScore = 0
            while j < len(nums):
                if ((num % 2 == 0) and (nums[j] % 2 != 0)) or ((num % 2 != 0) and (nums[j] % 2 == 0)):
                    currentScore += 1
                j += 1
            scores.append(currentScore)
        return scores
    
answer = Solution()
countOpposite = answer.countOppositeParity(nums = [1,2,3,4])
print(f"Count Opposite Parity: {countOpposite}")