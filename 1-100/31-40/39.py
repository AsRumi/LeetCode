from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return list(dict(sorted(Counter(nums).items(), key = lambda item: item[1], reverse = True)).keys())[:k]
    
answer = Solution()
top_element = answer.topKFrequent(nums = [1, 0, 3, 0], k = 1)
print(f"Top K Frequent Element: {top_element}")