# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeList(self, l1, l2):
        res = ListNode()
        cur = res

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2

        return res.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None   
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists

        return lists[0]

        # head = ListNode()
        # cur = head

        # while True:
        #     curMin = -1
        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             continue
        #         if curMin == -1 or lists[i].val < lists[curMin].val:
        #             curMin = i

        #     if curMin == -1:
        #         break

        #     cur.next = lists[curMin]
        #     lists[curMin] = lists[curMin].next
        #     cur = cur.next
            

        # return head.next
            