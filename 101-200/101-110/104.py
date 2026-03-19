"""
252. Meeting Rooms
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Convert to clean list.
        interval_list = []
        for interval in intervals:
            start, end = interval.start, interval.end
            interval_list.append((start, end))
        # Sort based on start times.
        interval_list.sort(key = lambda x : x[0])
        # Check overlap.
        i = 0
        while i < len(interval_list) - 1:
            if not (interval_list[i][1] <= interval_list[i + 1][0]):
                return False
            i += 1
        return True
    
answer = Solution()

interval1 = Interval(5, 8)
interval2 = Interval(9, 15)
interval_list = [interval1, interval2]

canAttendMeeting = answer.canAttendMeetings(interval_list)
print(f"Can Attend Meetings: {canAttendMeeting}")