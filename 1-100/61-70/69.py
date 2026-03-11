"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        head = ListNode()
        if list1.val < list2.val:
            head.val = list1.val
            list1 = list1.next
            head.next = list1
        else:
            head.val = list2.val
            list2 = list2.next
            head.next = list2
        start = head
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
                head = head.next
            else:
                head.next = list2
                list2 = list2.next
                head = head.next
        while list1:
            head.next = list1
            list1 = list1.next
            head = head.next
        while list2:
            head.next = list2
            list2 = list2.next
            head = head.next
        return start