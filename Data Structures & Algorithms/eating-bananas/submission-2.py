class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 

        l, r = 1, max(piles) 

        while l != r:
            mid = (l + r) // 2
            count = sum((p + mid - 1) // mid for p in piles)

            if count > h:
                l = mid + 1
            else:
                r = mid

        return l
