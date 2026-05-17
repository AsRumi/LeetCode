"""
Diameter of a Binary Tree: https://leetcode.com/problems/diameter-of-binary-tree/description/
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
        self.diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calls a helper function that calls itself recursively based on 3 conditions:\n
        If node has no left and right nodes:\t Return one edge count.\n
        If node has either left or right:\t Update global max and return one plus length of edges that are sent back recursively.\n
        If node has both:\t Find number of edges on either side and update global maximum; return one plus max of edges coming from either side.\n
        """
        def findDiameter(root):
            if (root.left is None) and (root.right is None):
                return 1
            if (root.left is None) or (root.right is None):
                if root.left is None: 
                    rightLength = findDiameter(root.right)
                    self.diameter = rightLength if rightLength > self.diameter else self.diameter
                    return 1 + rightLength
                else:
                    leftLength = findDiameter(root.left)
                    self.diameter = leftLength if leftLength > self.diameter else self.diameter
                    return 1 + leftLength
            else:
                leftLength = findDiameter(root.left)
                rightLength = findDiameter(root.right)
                sum = leftLength + rightLength
                self.diameter = sum if sum > self.diameter else self.diameter
                return max(1 + leftLength, 1 + rightLength)
        findDiameter(root)
        return self.diameter