# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        num_nodes = 0
        while cur:
            num_nodes += 1
            cur = cur.next

        num_divs = num_nodes // k

        cur = head
        res = ListNode()

        count = 0
        tail = cur

        divs = 0

        while cur and divs < num_divs: 
            local_tail = cur
            prev = None            
            inner_count = 0

            while inner_count < k:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                inner_count += 1 

            divs += 1

            count += inner_count

            if count <= k:
                res.next = prev 
            else:
                tail.next = prev
                tail = local_tail

        tail.next = cur

        return res.next
