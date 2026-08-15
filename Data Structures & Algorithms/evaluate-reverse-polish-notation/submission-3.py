class Solution:
    def eval(self, op1, op2, operator : str):
        if operator == "+":
            return op1 + op2
        elif operator == "-":
            return op1 - op2
        elif operator == "*":
            return op1 * op2
        elif operator == "/":
            return int(float(op1) / op2)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "/", "*"}
        stack = []
        for tok in tokens:
            if tok in operators:
                op2 = stack.pop()
                op1 = stack.pop()

                stack.append(self.eval(op1, op2, tok))
            else:
                stack.append(int(tok))

        return stack.pop()