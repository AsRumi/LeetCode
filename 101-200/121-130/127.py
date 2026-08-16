"""
23. Merge k Sorted Lists https://leetcode.com/problems/merge-k-sorted-lists/description/
"""

# Definition for singly-linked list.

from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # To avoid comparing k values every single time, you can use a heap to keep the items sorted naturally.
        heap = []

        dummy = ListNode(0, None)
        result = dummy

        for i, linkedList in enumerate(lists):
            # Returns the head of each list
            if linkedList:
                # Store the value and index of each list so that when heap compares for values for heapifying, and finds two items with the same value, it compares with indices instead. If it rather fell back to ListNodes, it would not be able to compare those items together and would crash.

                # You also need to push in the nodes themselves because you will use this node to find the next in sequence and add it in along with its value and list index.
                heap.append((linkedList.val, i, linkedList))

        # Perform one heapify operation to convert all current items in the list to a heap, instead of heappushing every first node. This makes the operation O(N) instead of O(N log N)
        heapq.heapify(heap)
        
        while heap:
            # Grab the smallest value from the heap:
            smallest, index, node = heapq.heappop(heap)

            # Create a node out of the smallest value and attach it to current result:
            curr = ListNode(smallest, None)
            result.next = curr
            result = result.next

            # From the list that was just used, advance the pointer and push the next node into the heap
            nxt = node.next
            if nxt:
                heapq.heappush(heap, (nxt.val, index, nxt))

        return dummy.next