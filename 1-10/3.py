import math
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        highest = max(candies)
        ans_list = []
        for i in candies:
            if(i+extraCandies >= highest):
                ans_list.append(True)
            else:
                ans_list.append(False)
        return ans_list
    
answer = Solution()
ans_list = answer.kidsWithCandies([1, 2, 3, 1, 5], 3)
print(ans_list)