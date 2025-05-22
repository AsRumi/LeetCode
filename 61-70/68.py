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
    
    def reverseList(self, head):
        head = self.createList(head)
        current = head
        
        return None
    
answer = Solution()
reversed_list = answer.reverseList(head = [1,2,3,4,5])
print(f"Reversed List: {reversed_list}")