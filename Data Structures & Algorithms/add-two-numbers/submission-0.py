# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        running = res
        carry = 0
        while l1 and l2:
            running.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            running = running.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            running.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            running = running.next
            l1 = l1.next

        while l2:
            running.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            running = running.next
            l2 = l2.next

        if carry:
            running.next = ListNode(carry)

        return res.next
