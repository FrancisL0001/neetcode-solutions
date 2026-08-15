class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', ']' : '[', '}' : '{'}
        
        for i in range(len(s)):
            if s[i] in pairs:
                if len(stack) < 1 or stack[-1] != pairs[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])

        return len(stack) == 0