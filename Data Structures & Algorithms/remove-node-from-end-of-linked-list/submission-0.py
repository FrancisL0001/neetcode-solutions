# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = left = head 
        prev = None

        right = head
        for i in range(n):
            right = right.next

        if not right:
            return res.next

        while right:
            right = right.next
            if not prev:
                prev = left
            else:
                prev = prev.next
            left = left.next

        if prev:
            prev.next = left.next
        

        return res

        