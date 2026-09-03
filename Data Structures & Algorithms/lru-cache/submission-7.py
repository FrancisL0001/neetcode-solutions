class ListNode:
    def __init__(self, key, value : int = 0):
        self.val = value
        self.key = key
        self.nxt = None
        self.prev = None
    
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.sz = 0
        self.cache = {}

        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)

        self.head.nxt, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            prev, nxt = node.prev, node.nxt
            prev.nxt, nxt.prev = nxt, prev

            prev, nxt = self.tail.prev, self.tail
            prev.nxt = nxt.prev = node
            node.prev, node.nxt = prev, nxt
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            new_node = self.cache[key]
            prev, nxt = new_node.prev, new_node.nxt
            prev.nxt, nxt.prev = nxt, prev
            new_node.val = value
        else:
            new_node = ListNode(key, value)
            self.sz += 1

        prev, nxt = self.tail.prev, self.tail
        prev.nxt = nxt.prev = new_node
        new_node.prev, new_node.nxt = prev, nxt
        self.cache[key] = new_node 

        if self.sz > self.capacity:
            lru = self.head.nxt
            nxt, prev = lru.nxt, lru.prev
            prev.nxt, nxt.prev = nxt, prev
            del self.cache[lru.key]
            self.sz -= 1

            



