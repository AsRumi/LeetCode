"""
98. Validate Binary Search Tree https://leetcode.com/problems/validate-binary-search-tree/description/
"""

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        To solve this problem, use a bottom-up approach. 
        Return information about the subtrees to the node in question, and find out if the current node makes for a valid binary search tree or not.
        The information is what the min and max is of a given node. 
        If this information is present with a node trying to figure out if it is the root of a valid BST or not, then it can do so in constant time.
        """
        
        def visit(node):
            
            if node is None:
                return (float('inf'), float('-inf'))
            
            # Traversing the tree before performing any operation is the same as performing operations bottom up
            leftValues = visit(node.left)
            rightValues = visit(node.right)
            
            # If a node has returned false, then propogate it without calculating anything for current node
            if leftValues is False or rightValues is False:
                return False
            
            # Check if current node is valid or not
            if leftValues[1] < node.val < rightValues[0]:
                # calculate what values will be returned if current node is valid
                minValue, maxValue = min(node.val, leftValues[0]), max(node.val, rightValues[1])
                return (minValue, maxValue)
            else:
                return False
            
        result = visit(root)
        
        return result is not False # if the root is a tuple, return True, else return False.