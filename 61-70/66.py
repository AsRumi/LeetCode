"""
3502. Minimum Cost to Reach Every Position

You are given an integer array cost of size n. You are currently at position n (at the end of the line) in a line of n + 1 people (numbered from 0 to n).

You wish to move forward in the line, but each person in front of you charges a specific amount to swap places. The cost to swap with person i is given by cost[i].

You are allowed to swap places with people as follows:

If they are in front of you, you must pay them cost[i] to swap with them.
If they are behind you, they can swap with you for free.
Return an array answer of size n, where answer[i] is the minimum total cost to reach each position i in the line.
"""

class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        minCost = cost[0]
        answer = []
        for i in cost:
            if i < minCost:
                minCost = i
            answer.append(minCost)
        return answer
    
answer = Solution()
minCosts = answer.minCosts(cost = [5,3,4,1,3,2])
print(f"Min Costs: {minCosts}")