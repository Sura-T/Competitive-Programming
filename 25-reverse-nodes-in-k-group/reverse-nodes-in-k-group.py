# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse_list(node):
            prev, cur = None, node
            while cur:
                next_temp = cur.next
                cur.next = prev
                prev = cur
                cur = next_temp
            return prev
      
        dummy = ListNode()
        dummy.next = head
        prev_group = dummy
      
        while head:
            count = 0
            cur = head
            while count < k and cur:
                cur = cur.next
                count += 1
          
            if count == k:
                kgroup_end = head
                for _ in range(k - 1):
                    kgroup_end = kgroup_end.next
                next_group = kgroup_end.next
                kgroup_end.next = None
                new_group_head = reverse_list(head)
              
                prev_group.next = new_group_head
                head.next = next_group
              
                prev_group = head
                head = next_group
            else:
                break
      
        return dummy.next