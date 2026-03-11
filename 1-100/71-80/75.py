"""
Balanced Binary Tree: https://leetcode.com/problems/balanced-binary-tree/
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.flag = False
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        This function calculates the depth at every node, starting from the root's right and left node.\n
        The checkHeight function checks the depth of the tree at every node on either side.\n
        If the depth of either side is greater than 1 compared to the other side, a global flag is set to True which means an unbalance is detected at a node which is not the root node.\n
        If no unbalance is detected throughout the tree, one final check is made at the end to see if there is an unbalance at the root node before returning a positive check.\n
        """
        if root is None:
            return True
        def checkHeight(root):
            if root is None:
                return 0
            leftHeight = checkHeight(root.left)
            rightHeight = checkHeight(root.right)
            if abs(leftHeight - rightHeight) > 1: 
                self.flag = True
            return 1 + max(leftHeight, rightHeight) # Returning 1 + maximum depth on either side because that is what causes imbalance.
        leftHeight, rightHeight = checkHeight(root.left), checkHeight(root.right)
        if self.flag:
            return False
        if abs(leftHeight - rightHeight) <= 1: return True
        return False