"""
1046. Last Stone Weight https://leetcode.com/problems/last-stone-weight/description/
"""

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x * -1 for x in stones]
        heap = stones
        heapq.heapify(heap)
        while len(heap) > 1:
            n1 = heapq.heappop(heap)
            n2 = heapq.heappop(heap)
            heapq.heappush(heap, abs(n1 - n2) * -1)
        return heap[0] * -1