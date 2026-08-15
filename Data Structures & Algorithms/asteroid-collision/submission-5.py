class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            else:
                cur = asteroids[i]
                prev = stack[-1]
                while cur * prev < 0 and cur < 0:
                    prev = stack.pop()
                    if abs(prev) != abs(cur):
                        cur = cur if (abs(cur) > abs(prev)) else prev
                        prev = stack[-1] if stack else 0
                    else:
                        cur = 0

                if cur:
                    stack.append(cur)
        
        return stack
