# 933. Number of Recent Calls

from collections import deque
class RecentCounter:
    
    def __init__(self):
        self.myQueue = deque()
        return

    def ping(self, t: int) -> int:
        self.myQueue.append(t)
        if len(self.myQueue) == 1:
            return 1
        while self.myQueue[0] < t-3000:
            self.myQueue.popleft()
        return len(self.myQueue)

myCounter = RecentCounter()
paramsList = [[1178],[1483],[1563],[4054],[4152],[6000],[7000]]
result = []
for param in paramsList:
    result.append(myCounter.ping(param[0]))

print(result)