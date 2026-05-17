"""
57. Insert Interval https://leetcode.com/problems/insert-interval/description/
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        newIntervalList = []
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newStart:
            newIntervalList.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        newIntervalList.append([newStart, newEnd])
        
        while i < len(intervals):
            newIntervalList.append(intervals[i])
            i += 1
        
        return newIntervalList
    
answer = Solution()
insert = answer.insert(intervals = [[1, 2],[3, 5],[6, 7],[12, 14],[15, 20]], newInterval = [4, 8])
print(f"Insert: {insert}")