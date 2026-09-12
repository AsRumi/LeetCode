"""
622. Design Circular Queue https://leetcode.com/problems/design-circular-queue/description/
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.queue = [0] * (k + 1)
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        
        # Check if full, then return False, otherwise insert it and move tail:
        if (self.tail == self.head - 1) or (self.head == 0 and self.tail == self.capacity):
            return False
        # Insert the element into the queue:
        self.queue[self.tail] = value
        self.tail += 1
        
        # Wrap around if tail overshoots:
        if self.tail > self.capacity:
            self.tail = 0
        
        return True

    def deQueue(self) -> bool:
        
        # If there is no element to delete:
        if self.head == self.tail:
            return False
        
        # Delete the element from the head position:
        self.head += 1 # just dereference
        
        # Wrap head around if it overshoots off the back:
        if self.head > self.capacity:
            self.head = 0
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        rear = self.tail - 1 if self.tail - 1 >= 0 else self.capacity
        return self.queue[rear]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return (self.tail == self.head - 1) or (self.tail == self.capacity and self.head == 0)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()