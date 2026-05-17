"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def createList(self, list):
        if not list:
            return None
        head = ListNode(list[0])
        current = head
        for values in list[1:]:
            current.next = ListNode(values)
            current = current.next
        return head
    
    def printList(self, head):
        current = head
        while(current.next):
            print(current.val)
            current = current.next
        print(current.val)
        return head
    
    def reverseLinkedListOptimal(self, head: Optional[ListNode]) -> ListNode:
        prev, temp, current = None, ListNode(), head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    
    def reverseList(self, head):
        head = self.createList(head)
        # head = self.printList(head)
        one = head
        if not one:
            return None
        two = one.next
        if not two:
            return head
        three = two.next
        if not three:
            one.next = None
            two.next = one
            return two
        one.next = None
        while(three):
            two.next = one
            one = two
            two = three
            three = three.next
        two.next = one
        return two
    
answer = Solution()
head = answer.createList(list = [1, 2, 3, 4, 5])
head = answer.reverseLinkedListOptimal(head = head)
print(f"Reversed Linked List: {answer.printList(head)}")