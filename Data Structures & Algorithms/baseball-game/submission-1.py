class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        runningSum = 0
        for op in operations:
            if op == "+":
                cur = stack[-1] + stack[-2]
                stack.append(cur)
                runningSum += cur
            elif op == "D":
                cur = stack[-1] * 2
                stack.append(cur)
                runningSum += cur
            elif op == "C":
                rem = stack.pop()
                runningSum -= rem
            else:
                stack.append(int(op))
                runningSum += int(op)

        return runningSum