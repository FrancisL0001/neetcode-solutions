class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)

        while n != 1:
            total = 0
            for d in str(n):
                total += int(d) ** 2
            if total in seen:
                return False 
            seen.add(total)
            n = total

        return True