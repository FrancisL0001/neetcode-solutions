# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        
        l, r = 0, n - 1
        
        prev, cur = head, head
        while l < r:
            count = 0
            while cur.next.next:
                cur = cur.next

            tail = cur.next
            cur.next = None
            tail.next = prev.next
            prev.next = tail

            prev = prev.next.next
            cur = prev

            l += 2

        