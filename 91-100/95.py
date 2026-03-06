"""
973. K Closest Points to Origin https://leetcode.com/problems/k-closest-points-to-origin/description/
"""

from typing import List
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(points_heap, (distance * -1, point))
            if len(points_heap) > k:
                heapq.heappop(points_heap)
        points = [x for _, x in points_heap]
        return points
    
answer = Solution()
kClosest = answer.kClosest([[3,3],[5,-1],[-2,4]], 2)
print(kClosest)