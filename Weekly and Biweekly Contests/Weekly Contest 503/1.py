from collections import Counter

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        nums_counter = Counter(nums)
        result = []
        for key, value in nums_counter.items():
            if value > k:
                nums_counter[key] = k
        for key, value in nums_counter.items():
            i = 0
            while i < value:
                i += 1
                result.append(key)
        return result
    
answer = Solution()
limitOccurence = answer.limitOccurrences(nums = [1,1,1,2,2,3], k = 2)
print(f"Limit Occurence: {limitOccurence}")