class MyHashSet:

    def __init__(self):
        self.values = {}

    def add(self, key: int) -> None:
        if isinstance(key, int):
            self.values[key] = 1
        else:
            raise "Invalid type for key"

    def remove(self, key: int) -> None:
        if key in self.values:
            self.values[key] = 0

    def contains(self, key: int) -> bool:
        return key in self.values and self.values[key] > 0


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)