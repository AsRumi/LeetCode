"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

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
reversed_list = answer.reverseList(head = [1, 2, 3, 4, 5])
print(f"Reversed List: {reversed_list}")