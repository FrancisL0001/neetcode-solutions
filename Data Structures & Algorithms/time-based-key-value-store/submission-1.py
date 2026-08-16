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
        if key not in self.store or self.store[key][0][0] > timestamp:
            return ""

        l, r = 0, len(self.store[key][0]) - 1
        while l < r:
            mid = (l + r) // 2
            if self.store[key][0][mid] == timestamp:
                return self.store[key][1][mid]
            elif self.store[key][0][mid] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        if self.store[key][0][l] <= timestamp:
            return self.store[key][1][l]
        else:
            return self.store[key][1][l - 1]