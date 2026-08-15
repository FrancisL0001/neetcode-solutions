class MyHashMap:

    def __init__(self):
        self.values = []

    def put(self, key: int, value: int) -> None:
        for kv in self.values:
            if kv[0] == key:
                kv[1] = value
                return
        self.values.append([key, value])

    def get(self, key: int) -> int:
        for [k, v] in self.values:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        new = []
        for [k,v] in self.values:
            if k != key:
                new.append([k,v])
        self.values = new


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)