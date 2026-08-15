from collections import deque

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dq = deque()
        count = {}

        for i in range(len(s)):
            dq.append(i)

            count[s[i]] = count.get(s[i], 0) + 1

        while dq and count[s[dq[0]]] > 1:
            dq.popleft()

        if dq:
            return dq[0]
        return -1