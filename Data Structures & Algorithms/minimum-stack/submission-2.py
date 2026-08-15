class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_ = val
        else:
            self.stack.append(val - self.min_)
            self.min_ = min(val, self.min_)
        

    def pop(self) -> None:
        if not self.stack:
            return 

        poped = self.stack.pop()
        if poped < 0:
            self.min_ = self.min_ - poped

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_
        else:
            return self.min_ + self.stack[-1]

    def getMin(self) -> int:
        return self.min_
