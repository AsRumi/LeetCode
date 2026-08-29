"""
102. Binary Tree Level Order Traversal https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""

# Definition for a binary tree node.

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        
        # put the nodes in a queue to process them level-wise
        queue = deque([root])

        while queue:
            no_nodes = len(queue)   # this level's size
            curr_result = []

            for _ in range(no_nodes):
                curr_node = queue.popleft()
                curr_result.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            result.append(curr_result)
        
        return result