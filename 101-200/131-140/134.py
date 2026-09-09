"""
1206. Design Skiplist https://leetcode.com/problems/design-skiplist/description/
"""

import math
import random

class ListNode:
    # __slots__ tells Python "instances of this class will ONLY ever have
    # these attributes." It means you CANNOT
    # do `node.some_new_field = 5` later -- only val/next/down are allowed.
    __slots__ = ('val', 'next', 'down')

    def __init__(self, val, next=None, down=None):
        self.val = val
        self.next = next # node to the right of this node on the same level
        self.down = down # node below this node (essentially the same number, just a different memory reference)

class Skiplist:
    def __init__(self):
        # A sentinel level that has -inf and +inf as its boundaries so every value falls between these nodes on this level
        level = ListNode(-math.inf, ListNode(math.inf))
        
        # A stack of entry points of each level. 
        # self.levels[-1] is the topmost level's leftmost -inf node.
        self.levels = [level]

    def search(self, target: int) -> bool:
        # Start at the top level's -inf sentinel.
        level = self.levels[-1]
        
        while level:
            node = level
            # Walk right on this level until you find a node that is greater than target.
            while node.next.val < target:
                node = node.next
            
            if node.next.val == target: # if found, return True
                return True
            
            # Otherwise drop down
            level = node.down
            
        return False # return False if you fall all the way down to the bottom without a match

    def add(self, num: int) -> None:
        # This stack holds rightmost nodes whose value is still < num, 
        # so that when you insert the node at the bottom-most level, 
        # you can access the nodes you need to stitch that node back to 
        # if the node is allowed to extend to that level.
        stack = []
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < num:
                node = node.next
            stack.append(node) # Record the predecessor node for this level.
            level = node.down

        heads = True # coin flip mechanism.
        down = None  # the node one level below the one we're about to make
        
        while stack and heads:
            prev = stack.pop()  # the predecessor node on this level
            node = ListNode(num, prev.next, down)
            prev.next = node
            down = node
            heads = random.randint(0, 1)

        # If we have used up every level we recorded in stack but coin still asks us to extend the node:
        if not stack and heads: 
            node = ListNode(num, ListNode(math.inf), down)
            level = ListNode(-math.inf, node, self.levels[-1])
            self.levels.append(level)

    def erase(self, num: int) -> bool:
        found = False
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < num:
                node = node.next
            if node.next.val == num: # If found, unlink on this level
                found = True
                node.next = node.next.next
            level = node.down # num might exist on multiple levels

        # Clean up: if the current top level's -inf sentinel now points
        # directly to the +inf sentinel, that means the top level has become empty because
        # we just erased its only element. In that case, pop it off
        # self.levels. `len(self.levels) > 1` guarantees we never remove the very last
        # remaining level -- there must always be at least a bottom level
        # to hold real data.
        while len(self.levels) > 1 and self.levels[-1].next.next is None:
            self.levels.pop()

        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
