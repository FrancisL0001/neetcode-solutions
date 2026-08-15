class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        l, r = 1, max(piles)
        total = sum(piles)

        while l != r:
            mid = (l + r) // 2
            count = 0
            countMinusOne = 0
            for p in piles:
                count += p//mid if p%mid == 0 else (p//mid + 1)
                countMinusOne += p//(mid-1) if p%(mid-1) == 0 else (p//(mid-1) + 1)

            if count <= h and countMinusOne > h:
                return mid
            elif count > h:
                l = mid + 1
            else:
                r = mid - 1

        return l
