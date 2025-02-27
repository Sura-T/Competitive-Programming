class ListNode:
    def __init__(self, value=0, next_node=None):
        self.val = value
        self.next = next_node

class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
      
        current = self.dummy.next
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
      
        predecessor = self.dummy
        for _ in range(index):
            predecessor = predecessor.next
      
        new_node = ListNode(val, predecessor.next)
        predecessor.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
      
        predecessor = self.dummy
        for _ in range(index):
            predecessor = predecessor.next
      
        to_delete = predecessor.next
        predecessor.next = to_delete.next
        to_delete.next = None
        self.size -= 1
     


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)