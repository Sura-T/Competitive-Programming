# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        count = 0
        temp = head

        while temp:
            start = temp.next
            count += 1
            temp = temp.next

        idx = count // 2

        while idx:
            head = head.next
            idx -= 1

        return head
