class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        
        def createClosest(nums):
            closest = []
            for i, num in enumerate(nums):
                if i == 0:
                    closest.append(1)
                elif i == len(nums) - 1:
                    closest.append(i - 1)
                else:
                    if abs(num - nums[i - 1]) <= abs(num - nums[i + 1]):
                        closest.append(i - 1)
                    else:
                        closest.append(i + 1)
            return closest
        
        closest = createClosest(nums)
        n = len(nums)
        
        # Use a prefix sum to store cumulative costs in both directions:
        forward = [0] * n
        for i in range(n - 1):
            if closest[i] == i + 1:
                forward[i + 1] = forward[i] + 1
            else:
                forward[i + 1] = forward[i] + (nums[i + 1] - nums[i])

        # Cumulative costs in backward direction:
        backward = [0] * n
        for i in range(n - 1, 0, -1):
            if closest[i] == i - 1:
                backward[i - 1] = backward[i] + 1
            else:
                backward[i - 1] = backward[i] + (nums[i] - nums[i - 1])

        # Process queries based on direction of traversal using prefix sum:
        ans = []
        for l, r in queries:
            if l < r:
                ans.append(forward[r] - forward[l])
            else:
                ans.append(backward[r] - backward[l])

        return ans
    
answer = Solution()
minCost = answer.minCost(nums = [0, 2, 3, 9], queries = [[3,0],[1,2],[2,0]])
print(f"Minimum Cost: {minCost}")