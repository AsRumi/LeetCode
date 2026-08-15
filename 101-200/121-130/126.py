"""
25. Reverse Nodes in k-Groups https://leetcode.com/problems/reverse-nodes-in-k-group/editorial/
"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        """
        Just like the previous problem where you had to reverse a particular section, 
        here you need to reverse groups of k nodes, starting with head.

        Eg: 
        List: 1->2->3->4->5->6 k=3
        Output: 3->2->1->6->5->4

        The approach is to walk k nodes first to check if they exist, 
        if they do, move the anchor and reverse the section;
        if they don't, return the remainder as it is
        """

        dummy = ListNode(0, head)
        anchor = dummy

        while True:
            # First, verify that there are k-nodes remaining:
            kth = anchor
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next # Save first node of the next section

            """
            In a simple linked-list reversal, you set the first node's next to None
            because after reversal, that node becomes the last node and must point to None.
            But here, the first node needs to point to the starting node of the next section, therefore;
            you set it to group_next instead.
            """
            prev, curr = group_next, anchor.next
            while curr is not group_next: # Reverse only till the section that needs to be reversed.

                # reverse using temp variable and advance
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt

            # to understand this, understand what the nodes have now become
            tail = anchor.next # anchor.next still points to the same old beginning node of the section
            anchor.next = kth # kth is the group's old last, which is now the group's new first
            anchor = tail # move the anchor to one before the new section