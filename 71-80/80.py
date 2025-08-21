"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        lengthChecker = head
        while(lengthChecker):
            length += 1
            lengthChecker = lengthChecker.next
        target = length - n + 1
        prev = None #Edge: Length = 1
        originalHead = head
        while(target > 1):
            target -= 1
            prev = head
            head = head.next
        if prev is None:
            if head.next is None:
                return prev
            else: 
                """
                Block to solve for first element needs to be skipped.
                """
                originalHead = head.next
                return originalHead
        if head.next is None:
            prev.next = None
        else:
            prev.next = head.next
        return originalHead