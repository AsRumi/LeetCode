"""
3885. Design Event Manager https://leetcode.com/problems/design-event-manager/description/
"""

import heapq

class EventManager:

    def __init__(self, events: list[list[int]]):
        self.event_hashmap = {}
        self.event_list = []
        for eventId, priority in events:
            self.event_hashmap[eventId] = priority
            self.event_list.append((priority * -1, eventId))
        heapq.heapify(self.event_list)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.event_hashmap[eventId] = newPriority
        heapq.heappush(self.event_list, (newPriority * -1, eventId))

    def pollHighest(self) -> int:
        while True:
            if len(self.event_list) > 0:
                popPriority, popEventId = heapq.heappop(self.event_list)
                if self.event_hashmap.get(popEventId) and self.event_hashmap[popEventId] == popPriority * -1:
                    self.event_hashmap.pop(popEventId)
                    return popEventId
            else:
                return -1


# Your EventManager object will be instantiated and called as such:
obj = EventManager([[5,7],[2,7],[9,4]])
print(obj.pollHighest())
obj.updatePriority(9, 7)
print(obj.pollHighest)
print(obj.pollHighest)