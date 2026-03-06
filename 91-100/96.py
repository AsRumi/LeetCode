"""
215. Kth Largest Element in an Array https://leetcode.com/problems/kth-largest-element-in-an-array/description/
"""

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, num)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            print(f"After {num}: {max_heap}")
        return max_heap[0]
    
answer = Solution()
kthLargest = answer.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4)
print(kthLargest)