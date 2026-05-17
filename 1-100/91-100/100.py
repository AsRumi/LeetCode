"""
133. Clone Graph https://leetcode.com/problems/clone-graph/description/
"""

from typing import Optional

# Definition of Node class:

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def clone_node(node: Node, clone: Node):
            for neighbor in node.neighbors:
                if neighbor.val not in cloned_hashmap.keys():
                    cloned_neighbor = Node(neighbor.val)
                    clone.neighbors.append(cloned_neighbor)
                    cloned_hashmap[cloned_neighbor.val] = cloned_neighbor
                    clone_node(neighbor, cloned_neighbor)
                else:
                    clone.neighbors.append(cloned_hashmap[neighbor.val])
        
        if node is None:
            return None
        
        cloned_hashmap = {}
        cloned_first = Node(node.val)
        
        cloned_hashmap[cloned_first.val] = cloned_first
        clone_node(node, cloned_first)
        return cloned_first
    
answer = Solution()
cloneGraph = answer.cloneGraph()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.append(node2)
node1.neighbors.append(node4)

node2.neighbors.append(node1)
node2.neighbors.append(node3)

node3.neighbors.append(node2)
node3.neighbors.append(node4)

node4.neighbors.append(node1)
node4.neighbors.append(node3)