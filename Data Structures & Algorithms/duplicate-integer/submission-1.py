class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for num in nums:
            if not num in seen:
                seen.append(num)
            else:
                return True
        return False
