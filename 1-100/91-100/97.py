"""
621. Task Scheduler https://leetcode.com/problems/task-scheduler/
"""

from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frame_size = n + 1
        task_frequencies = Counter(tasks)
        sorted_frequencies = sorted(task_frequencies.items(), key = lambda item: item[1], reverse = True)
        sorted_frequencies = dict(sorted_frequencies)
        top_frequencies = 0
        max_frequency = -1
        for value in sorted_frequencies.values():
            if max_frequency <= value:
                max_frequency = value
                top_frequencies += 1
            else: 
                break
        slots = (max_frequency - 1) * (frame_size) + top_frequencies
        return max(len(tasks), slots)
    
answer = Solution()
leastInterval = answer.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)
print(f"Least Interval: {leastInterval}")