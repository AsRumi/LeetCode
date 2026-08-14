"""
141. Linked List Cycle https://leetcode.com/problems/linked-list-cycle/description/
"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # To check if a singly-linked list has a cycle or not, use Floyd's Tortoise and Hare algorithm
        # Intuition: in a cycle, fast pointer gains one step over slow and eventually intersects
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False

    # If you also want to find out where the cycle began, 
    # reset one pointer to head when they first intersect.
    # The second point of intersection is where the cycle begins.
    def detect_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                slow = head # reset slow to head and move them one step at a time until they intersect again
                while slow is not fast:
                    slow, fast = slow.next, fast.next
                return slow
        return None