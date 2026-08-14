"""
19. Remove Nth Node From End of List https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # For this solution, use a fast pointer and a slow pointer
        # Keep the fast pointer at an offset of n from the slow one
        # When fast reaches the end, slow pointer is nth from the end

        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next # fast is now at an offset of n from the beginning

        while fast.next: # now go until fast reaches the end
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next