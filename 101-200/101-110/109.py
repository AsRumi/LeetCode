"""
846. Hand of Straights https://leetcode.com/problems/hand-of-straights/description/
"""

from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_dict = {}
        for number in hand:
            if hand_dict.get(number) is not None:
                hand_dict[number] += 1
            else:
                hand_dict[number] = 1
        hand_list = []
        for key, value in hand_dict.items():
            hand_list.append([key, value])
        
        hand_list.sort()
        
        while len(hand_list):
            i = 0
            popped = 0
            last_inserted = None
            while i < groupSize:
                if i == 0:
                    hand_list[i][1] -= 1
                    last_inserted = hand_list[i][0]
                    if hand_list[i][1] == 0:
                        hand_list.pop(i)
                        popped += 1
                else:
                    if len(hand_list) == 0 or hand_list[i][0] - last_inserted != 1 or i > len(hand_list):
                        return False
                    else:
                        
                i += 1 - popped
        
        return False
    
answer = Solution()
isNStraightHand = answer.isNStraightHand(hand = [1,3,6,2,2,3,4,7,8], groupSize = 3)
print(f"Is N Straight Hand: {isNStraightHand}")