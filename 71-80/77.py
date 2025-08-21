"""
Subtree of another tree: https://leetcode.com/problems/subtree-of-another-tree/description/
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        This function employs a helper function (which compares and checks if two trees are same, exactly as the solution in 76.py).\n
        It simply traverses the nodes in DFS manner and sends the nodes for a tree check if the values are the same.\n
        If the tree check does not return True, pop the node and add its children to the stack.\n
        Repeat the process until either there are no more children to add to the stack, or the subtree is found.
        """
        def isSameTree(p, q):
            if (p is None) and (q is None):
                return True
            elif (p is None) and not(q is None):
                return False
            elif not(p is None) and (q is None):
                return False
            if (p.val == q.val):
                if isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
                    return True
                else:
                    return False
            else:
                return False
        
        #None Checks
        if (root is None) and not(subRoot is None):
            return False
        elif (root is None) and (subRoot is None):
            return True
        
        root_stack = []
        root_stack.append(root)
        while len(root_stack) != 0:
            p = root_stack[-1]
            if p.val == subRoot.val:
                if isSameTree(p, subRoot):
                    return True
            root_stack.pop()
            if p.right:
                root_stack.append(p.right)
            if p.left:
                root_stack.append(p.left)
        return False