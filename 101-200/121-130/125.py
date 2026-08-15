"""
92. Reverse Linked List II https://leetcode.com/problems/reverse-linked-list-ii/description/
"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # To reverse a portion of a linked list, you need two things; 
        # a pointer to the node right before the section, and to the starting node of the section

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next # Move to the node that is one before the section you want to switch

        curr = prev.next # Store the node that is the start of this section

        """
        Now what you want to do is take every node that comes after curr 
        and shift that node to the beginning (which is right after prev) of the section.

        Do this for every node, keeping curr in its place, 
        and moving every node that comes after it to the front. 

        This will automatically flip the section.
        """

        for _ in range(right - left):
            nxt = curr.next # Store the node that comes after current node 
            # (this is the node that you will bring to the front of the section)

            curr.next = nxt.next # Make the current node skip nxt and go to the node one further

            nxt.next = prev.next # Insert the skipped node at the starting position

            """
            You use prev.next instead of curr (even though they are the same during the first pass)
            because they are not the same afterwards, curr stays the same, 
            whereas prev.next always points to the node that is at the start of the section at this moment.
            """

            prev.next = nxt # Make previous point to current starting node of section that needs to be reversed

        return dummy.next