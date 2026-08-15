class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigits(num : int) -> int:
            return sum([(int(d))**2 for d in str(num)])

        seen = {}

        cur = sumDigits(n)
        while not cur in seen:
            if cur == 1:
                return True
            else:
                seen[cur] = 1
                cur = sumDigits(cur)

        return False 