"""
230. Kth Smallest Element in a BST https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
"""

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Using the property of a BST, the smallest element in the tree is the left-most node.
        The second smallest node is the smallest node's parent. 
        The third smallest node is the minimum in the second smallest node's right subtree.
        
        This pattern reoccurs throughout the tree; repeat it k number of times to get the kth smallest number.
        """
    
        stack = [] # Have a stack to remember the nodes that you encountered along the path so you can recurse upwards.
        node = root

        while stack or node:
            # dive to the leftmost node, remembering the path
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            # successor: right subtree, the while loop then takes you to the leftmost of it in its next iteration
            node = node.right

        return -1