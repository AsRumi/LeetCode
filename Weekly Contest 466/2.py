class Solution:
    def minOperations(self, s: str) -> int:
        cost = {}
        start = 25
        for i in range(98, 123):
            cost[chr(i)] = start
            start -= 1
        for key in cost.keys():
            if key in s:
                return cost[key]
        return 0
    
ans = Solution()
minOperations = ans.minOperations(s = "abcdef")
print(minOperations)