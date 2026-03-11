# 649. Dota2 Senate
from collections import deque
class Solution:
    def __init__(self):
        self.rq = deque()
        self.dq = deque()
        self.r_debt = 0
        self.d_debt = 0
    def predictPartyVictory(self, senate: str) -> str:
        for senator in senate:
            if senator == "R":
                self.rq.append('R')
            else:
                self.dq.append('D')
        for senator in senate:
            if senator == "R":
                self.d_debt += 1
            else:
                self.r_debt += 1
            
        return "Radiant"
    
answer = Solution()
predicted_party = answer.predictPartyVictory(senate = 'RDDRD')
