"""
235. Lowest Common Ancestor of a Binary Search Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Using properties of BST, there are 4 fundamental check conditions to be made.\n
        The bounding properties of the problem statement gives us some relief on edge cases.\n
        If the root is either one of the values, or is between the values, then that is the LCA.\n
        If the root is greater than both the values, the then LCA lies to the left.\t Else to the right.
        """
        if root.val == p.val or root.val==q.val:
            return root
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
    