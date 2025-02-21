# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller, greater = ListNode(), ListNode()
        pt1, pt2 = smaller, greater

        while head:
            if head.val < x:
                pt1.next = head
                pt1 = pt1.next
            else:
                pt2.next = head
                pt2 = pt2.next
            head = head.next

        pt1.next = greater.next
        pt2.next = None

        return smaller.next

        

