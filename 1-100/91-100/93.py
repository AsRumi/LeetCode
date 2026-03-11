"""
703. Kth Largest Element in a Stream https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
"""

from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.priority = nums
        heapq.heapify(self.priority)
        while len(self.priority) > k:
            heapq.heappop(self.priority)

    def add(self, val: int) -> int:
        heapq.heappush(self.priority, val)
        if len(self.priority) > self.k:
            heapq.heappop(self.priority)
        return self.priority[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

obj = KthLargest(4, [7, 7, 7, 7, 8, 3])
print(obj.add(2))
print(obj.add(10))
print(obj.add(9))
print(obj.add(9))