# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        res = []

        while curr is not None:
            res.append(curr.val)
            curr = curr.next

        while head is not None:
            x = res.pop()

            if head.val != x:
                return False
            head = head.next

        return True
        

        

        
        