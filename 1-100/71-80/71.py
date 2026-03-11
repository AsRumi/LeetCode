"""
143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseLinked(self, head: Optional[ListNode]) -> ListNode:
        prev, temp = None, ListNode()
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def mergeLinked(self, first: Optional[ListNode], second: Optional[ListNode]) -> ListNode:
        head = first
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        return head

    def reorderList(self, head: Optional[ListNode]) -> ListNode:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while(fast.next):
            slow = slow.next
            fast = fast.next
            if(fast.next):
                fast = fast.next
            else:
                break
        second = slow.next
        slow.next = None

        second = self.reverseLinked(second)
        first = head
        
        result = self.mergeLinked(first, second)
        return result