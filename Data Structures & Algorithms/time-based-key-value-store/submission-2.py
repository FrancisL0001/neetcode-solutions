class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key][0].append(timestamp)
            self.store[key][1].append(value)
        else:
            self.store[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        l, r = 0, len(self.store[key][0]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if self.store[key][0][mid] <= timestamp:
                res = self.store[key][1][mid]
                l = mid + 1 
            else:
                r = mid - 1

        return res