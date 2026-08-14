"""
21. Merge Two Sorted Lists https://leetcode.com/problems/merge-two-sorted-lists/description/
"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Use the tail append method
        # Compare values from two lists and append them to the end of the resultant list
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                # Add list1's current node, move list1 one ahead
                tail.next = list1
                list1 = list1.next
            else:
                # Add list2's current node, move list2 one ahead
                tail.next = list2
                list2 = list2.next

            # Move tail one ahead
            tail = tail.next
        
        # Append the remaining from whichever list is not exhausted
        tail.next = list1 or list2

        # Return the head of the resultant linked list
        return dummy.next