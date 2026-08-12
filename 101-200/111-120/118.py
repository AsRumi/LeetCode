"""
239. Sliding Window Maximum https://leetcode.com/problems/sliding-window-maximum/description/
"""

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Set-up the data structures and variables to use:
        dq = deque() # This is a deque which stores the indices of nums in non-increasing order
        result = [] # To store all results
        
        for i, num in enumerate(nums):
            
            # If there are elements in the deque, remove all those (from the right) that are lesser than current num
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            # Now current num goes in its right place, which is the end of the deque, being the smallest element in the deque
            dq.append(i)
            # The largest element of the deque is always at the front of the deque
            
            # Remove the element that just went out of the window
            if dq[0] <= i - k:
                dq.popleft()
            
            # You can only compute the first max if you have seen 0 to k-1 elements so far
            # Start firing after you hit k-1
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
    
answer = Solution()
maxSlidingWindow = answer.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
print(f"Max Sliding Window: {maxSlidingWindow}")