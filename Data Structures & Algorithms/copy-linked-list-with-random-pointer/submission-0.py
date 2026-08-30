"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        buff = {None : None}

        cur = head

        while cur:
            copy = Node(cur.val)
            buff[cur] = copy
            cur = cur.next

        cur = head 
        while cur:
            copy = buff[cur]
            copy.next = buff[cur.next]
            copy.random = buff[cur.random]
            cur = cur.next

        return buff[head]


        
