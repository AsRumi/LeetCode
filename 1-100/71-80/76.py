"""
Same Tree: https://leetcode.com/problems/same-tree/description/
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        This function calls itself recursively, after comparing the values of the two nodes at the current point in the tree, using the children nodes.\n
        It triggers a False that propogates in the call stack is a value mismatch or a structure mismatch is found. If no False is returned, the two trees are same.
        """
        # None checks
        if (p is None) and (q is None):
            return True
        elif (p is None) and not(q is None):
            return False
        elif not(p is None) and (q is None):
            return False
        # If
        if (p.val == q.val):
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        # Else
        else:
            return False
    
p = TreeNode(1)
pl = TreeNode(2)
pr = TreeNode(3)
q = TreeNode(1)
ql = TreeNode(2)
qr = TreeNode(3)

p.left = pl
p.right = pr
q.left = ql
q.right = qr

answer = Solution()
isSameTree = answer.isSameTree(p, q)
print(f"Is Same Tree: {isSameTree}")