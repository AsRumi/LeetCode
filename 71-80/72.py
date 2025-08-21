"""
226. Invert Binary Tree https://leetcode.com/problems/invert-binary-tree/description/
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        stack = []
        stack.append(root)
        while len(stack) != 0:
            node = stack[-1]
            temp = node.left
            node.left = node.right
            node.right = temp
            stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return root