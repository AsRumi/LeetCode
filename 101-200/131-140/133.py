"""
146. LRU Cache https://leetcode.com/problems/lru-cache/description/
"""

class Node:
    
    def __init__(self, prev, nxt, data):
        self.prev = prev
        self.next = nxt
        self.data = data
        
class LinkedList:
    
    def __init__(self):
        self.head = Node(prev = None, nxt = None, data = None)
        self.tail = Node(prev = self.head, nxt = None, data = None)
        self.head.next = self.tail

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        
        self.linkedList = LinkedList()
        self.lookupDict = {}


    def get(self, key: int) -> int:
        
        # If key exists, return the key and push it to the tail. 
        # If it does not exist, return -1.
        if key in self.lookupDict.keys():
            currentNode = self.lookupDict[key]
            if currentNode.next == self.linkedList.tail:
                pass
            else:
                tempPrev = currentNode.prev
                tempNext = currentNode.next
                
                # Move the current node to the end.
                temp = self.linkedList.tail.prev
                self.linkedList.tail.prev = currentNode
                currentNode.next = self.linkedList.tail
                currentNode.prev = temp
                temp.next = currentNode
                
                # Fill the cavity the current node left when it moved from its original location.
                tempPrev.next = tempNext
                tempNext.prev = tempPrev
            
            return currentNode.data[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        # If the key is already present, then you do not need to insert, 
        # just move the key to the last position:
        if key in self.lookupDict.keys():
            currentNode = self.lookupDict[key] # get the node
            currentNode.data = (key, value) # update its key-value pair with the given new value
            
            # If the node is already the last one in the linkedlist: 
            if currentNode.next == self.linkedList.tail:
                pass
            else:
                tempPrev = currentNode.prev
                tempNext = currentNode.next
                
                # Move the current node to the end.
                temp = self.linkedList.tail.prev
                self.linkedList.tail.prev = currentNode
                currentNode.next = self.linkedList.tail
                currentNode.prev = temp
                temp.next = currentNode
                
                # Fill the cavity the current node left when it moved from its original location.
                tempPrev.next = tempNext
                tempNext.prev = tempPrev
            
        # Else, if there is a need to insert the key, first check if there is capacity,
        # if there is, simply insert at the end, else first remove from head, then insert at the end:
        else:
            # Remove from head if there is no capacity:
            if self.length == self.capacity:
                temp = self.linkedList.head.next.next
                toPop = self.linkedList.head.next # store the node being removed because you need it to remove the entry from the dict
                self.linkedList.head.next = temp
                temp.prev = self.linkedList.head
                self.lookupDict.pop(toPop.data[0]) # remove the node from the lookup dict
            
            # Add item into linked list:
            currentNode = Node(None, None, (key, value))
            
            temp = self.linkedList.tail.prev
            self.linkedList.tail.prev = currentNode
            currentNode.next = self.linkedList.tail
            currentNode.prev = temp
            temp.next = currentNode
            
            # Add item into the dict with a reference:
            self.lookupDict[key] = currentNode
            self.length = self.length + 1 if self.length < self.capacity else self.length
                
        return None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)