"""
57. Insert Interval https://leetcode.com/problems/insert-interval/description/
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        newIntervalList = []
        setMin, setMax = 0, None
        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            if end < newStart:
                newIntervalList.append([start, end])
            else:
                break
            i += 1
        start, end = intervals[i]
        setMin = min(start, newStart)
        print(f"Set Min calculated as: {setMin}\ni is {i}\nstart is {start}")
        while i < len(intervals) and newEnd > start:
            start, _ = intervals[i]
            i += 1
        i = i - 2
        _, end = intervals[i]
        setMax = max(end, newEnd)
        newIntervalList.append([setMin, setMax])
        i += 1
        while i < len(intervals):
            newIntervalList.append(intervals[i])
            i += 1
        return newIntervalList
    
answer = Solution()
insert = answer.insert(intervals = [[1, 2],[3, 5],[6, 7],[12, 14],[15, 20]], newInterval = [4, 8])
print(f"Insert: {insert}")