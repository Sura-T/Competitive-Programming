class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.deque = deque()
    
    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.appendleft(value)
            return True
        return False
    
    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        return False
    
    def deleteFront(self) -> bool:
        if self.deque:
            self.deque.popleft()
            return True
        return False
    
    def deleteLast(self) -> bool:
        if self.deque:
            self.deque.pop()
            return True
        return False
    
    def getFront(self) -> int:
        return self.deque[0] if self.deque else -1
    
    def getRear(self) -> int:
        return self.deque[-1] if self.deque else -1
    
    def isEmpty(self) -> bool:
        return len(self.deque) == 0
    
    def isFull(self) -> bool:
        return len(self.deque) == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()