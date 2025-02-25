# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        a = head
        b = head.next
        c = head.next
        while b and b.next:
            a.next = b.next
            a = a.next

            b.next = a.next
            b = b.next

        a.next = c

        return head