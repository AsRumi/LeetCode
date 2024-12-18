# 217. Contains Duplicate
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count = Counter(nums)
        count = count.most_common()
        if count[0][1]>1:
            return True
        return False
    
answer = Solution()
contains = answer.containsDuplicate(nums = [1,2,3,1])
print(f"Contains Duplicate: {contains}")