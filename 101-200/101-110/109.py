"""
846. Hand of Straights https://leetcode.com/problems/hand-of-straights/description/
"""

from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        return False
    
answer = Solution()
isNStraightHand = answer.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3)
print(f"Is N Straight Hand: {isNStraightHand}")