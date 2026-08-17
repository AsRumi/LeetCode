"""
572. Subtree of Another Tree https://leetcode.com/problems/subtree-of-another-tree/description/
"""

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        To check if a given tree has the given subtree or not, 
        start with every node and check if the given node is the subtree you are looking for or not.

        This is a O(n.m) solution. Which is correct but slow.

        To make this solution faster, convert the trees to strings and go for a fast substring search algorithm (KMP).
        However, when you convert the tress to substrings, use Preorder traversal and add # in place of nulls.
        Also add delimiters before you add every node's value because: "12, #, 5, 6, 2, 3" and "2, #, 5, 6, 2, 3"
        returns True (as valid substrings), however there is no node 2 in the original tree.
        Therefore adding delimiters turns the strings into ", 12, #, 5, 6, 2, 3" and ", 2, #, 5, 6, 2, 3"
        which now correctly returns false.
        """
        def isSameTree(p, q):

            def testNode(a, b):
                if a and b and a.val == b.val:
                    return True
                if not a and not b:
                    return True
                else:
                    return False

            if not testNode(p, q):
                return False
            if not p and not q:
                return True
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        if isSameTree(root, subRoot):
            return True
        else:
            if root:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            else:
                return False

